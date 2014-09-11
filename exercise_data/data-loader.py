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
        self.url = esurl
        self.conn = pyes.ES(esurl, timeout=60, bulk_size=10)



    #loads single records over http using urllib2
    def simpleHttpLoad(self, esurl, id, query):

        try:
            opener = urllib2.build_opener(urllib2.HTTPHandler)
            request = urllib2.Request(esurl+id, data=query)
            request.add_header('Content-Type', 'application/json')
            request.get_method = lambda: 'PUT'
            url = opener.open(request)
        except Exception as e:
            logging.error(e)

    def createPercolator(self, url, key, geometry):

        query = '{"query": {"geo_shape": {"location": {"shape": '+geometry+' } } }, "type": "location"}'
        self.simpleHttpLoad(url,key,query)

    def validateGeometry(self, geom):
        from shapely.validation import explain_validity
        if (explain_validity(geom) == 'Valid Geometry'):
            return True
        else:
            return False

    def simplifyGeometry(self, geom, tolerance):
        logging.info('Simplifying Geometry') 
        return geom.simplify(tolerance, preserve_topology=False)

    def processData(self,esindex, estype,  shpPath, keyField, simplify, tolerance, startfrom, limit, addPoint, createPercolator,percolatorkey):
        

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

                            # add point to data
                            if(addPoint==True):
                                pnt = geom.representative_point()
                                pnt_dict = {'point_location': '{0},{1}'.format(pnt.x,pnt.y)}
                                f.update(pnt_dict)
                                pnt_dict_bettermap = {'point_location_bettermap': [pnt.x,pnt.y]}
                                f.update(pnt_dict_bettermap)
                            
                            data = json.dumps(f)
                            key = f[keyField]

                            #normal index
                            if(createPercolator!=True):
                                self.conn.index(data,esindex,estype,key)

                            #percolator
                            if(createPercolator==True):
                                suburbkey = f["properties"][percolatorkey].replace(" ", "_")
                                geomAsJson=json.dumps(f['geometry'])
                                url = "http://{0}/{1}/.percolator/".format(self.url,esindex)
                                self.createPercolator(url,suburbkey,geomAsJson)
                            
                            
                        else:
                            logging.error('Invalid Geometry: ' + f[keyField]) 

                    cnt = cnt+1
        except:
            raise

if __name__ == '__main__':

        #grab the args
        parser = argparse.ArgumentParser(description='Load data into Elastic Search')
        parser.add_argument('esurl', metavar='rooturl', type=str, help='Root url of elastic search, including index and type')
        parser.add_argument('esindex', metavar='esindex', type=str, help='The elasticsearch index you are loading into')
        parser.add_argument('estype', metavar='estype', type=str, help='The elasticsearch type your loading into')
        parser.add_argument('shpPath', metavar='shpPath', type=str, help='Path to the shapefile')
        parser.add_argument('keyField', metavar='keyField', type=str, help='Primary key field name')
        


        parser.add_argument('--simplify', action='store_true', help='Whether to simplify the geometry')
        parser.add_argument('--tolerance', metavar='tolerance', type=float, help='simplification tolerance distance')
        parser.add_argument('--startfrom', metavar='startfrom', type=int, help='an index to start the load from')
        parser.add_argument('--limit', metavar='limit', type=int, help='record limit')
        parser.add_argument('--addPoint', action='store_true', help='Push a representative point into elasticsearch')
        parser.add_argument('--createPercolator', action='store_true', help='Create a percolator index')
        parser.add_argument('--percolatorkey', type=str, help='Percolator key')


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
        addPoint = args.addPoint
        createPercolator = args.createPercolator
        percolatorkey = args.percolatorkey

        loader = loader(esurl)
        loader.processData(esindex, estype, shpPath, keyField, simplify, tolerance, startfrom, limit, addPoint, createPercolator, percolatorkey)
