# #################################################################################
#  data-loader
#  Author: Simon Hope - Geoplex - September 2013
#
#  Loads a shapefile into an Elastic Search Index. Assumes Elastic search index, type and mapping has been set up to match the schema of the shapefile
#
#
# #################################################################################

import sys, argparse
import fiona
import shapely
import json
import urllib2
import logging
import pyes

logging.basicConfig(filename='data-loader.log',level=logging.DEBUG)


class loader:

    def __init__(self,esurl):
        #open the es connection
        self.conn = pyes.ES(esurl, timeout=60, bulk_size=10)



    #loads single records over http using urllib2
    def simpleHttpLoad(esurl, f):

        try:
            logging.info('Pushing to: '+ esurl+f['id']) 
            opener = urllib2.build_opener(urllib2.HTTPHandler)
            request = urllib2.Request(esurl+f['id'], data=json.dumps(f))
            request.add_header('Content-Type', 'application/json')
            request.get_method = lambda: 'PUT'
            url = opener.open(request)
        except Exception as e:
            logging.error(e)


    def validateGeometry(self, geom):
        from shapely.validation import explain_validity
        if (explain_validity(geom) == 'Valid Geometry'):
            return True
        else:
            return False

    def simplifyGeometry(self, geom, tolerance):
        logging.info('Simplifying Geometry') 
        return geom.simplify(tolerance, preserve_topology=False)

    def processData(self,esindex, estype,  shpPath, keyField, simplify, tolerance, startfrom, limit):
        

        # Open a file for reading
        try:
           with open(shpPath): pass
        except IOError:
           print 'Unable to locate file: ' + shpPath

        #check that a tolerance is passed when simplifying.
        if(simplify==True):
            if (tolerance==None):
                raise ValueError('You must pass a valid tolerance if simplifying geometry') 

        #use fiona to open the shapefile and read it
        try:    
            with fiona.open(shpPath) as source:

                cnt=1
                for f in source:
                    
                    if(cnt > limit):
                        return

                    featid = int(f[keyField])
                    if(featid > startfrom):
                    
                        #grab the geom
                        from shapely.geometry import shape
                        geom = shape(f['geometry'])

                        #simplify if required
                        if (self.validateGeometry(geom)):
                            if(simplify==True):
                                geom = simplifyGeometry(geom, tolerance)
                        
                        #if the geom is valid then push it into es
                        if (self.validateGeometry(geom)):
                            data = json.dumps(f)
                            key = f[keyField]

                            self.conn.index(data,esindex,estype,key)
                            
                        else:
                            logging.error('Invalid Geometry: ' + f[keyField]) 

                    cnt = cnt+1
        except:
            raise

if __name__ == '__main__':

        #grab the args
        parser = argparse.ArgumentParser(description='Load data into Elastic Search')
        parser.add_argument('esurl', metavar='rooturl', type=str, help='Root url of elastic search, including index and type')
        parser.add_argument('esindex', metavar='esindex', type=str, help='The elastic search index you are loading into')
        parser.add_argument('estype', metavar='estype', type=str, help='The elastic search type your loading into')
        parser.add_argument('shpPath', metavar='shpPath', type=str, help='Path to the shapefile')
        parser.add_argument('keyField', metavar='keyField', type=str, help='Primary key field name')

        parser.add_argument('--simplify', action='store_true', help='Whether to simplify the geometry')
        parser.add_argument('--tolerance', metavar='tolerance', type=float, help='simplification tolerance distance')
        parser.add_argument('--startfrom', metavar='startfrom', type=int, help='an index to start the load from')
        parser.add_argument('--limit', metavar='limit', type=int, help='record limit')


        args = parser.parse_args()

        esurl = args.esurl
        esindex = args.esindex
        estype = args.estype
        shpPath = args.shpPath
        keyField = args.keyField
        simplify = args.simplify
        tolerance = args.tolerance
        startfrom = args.startfrom
        limit = args.limit

        loader = loader(esurl)
        loader.processData(esindex, estype, shpPath, keyField, simplify, tolerance, startfrom, limit)