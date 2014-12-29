#!/usr/bin/env bash

#load data script
curl -XPUT 'http://127.0.01:9200/suburbs/'
curl -XPUT '127.0.01:9200/suburbs/_mapping/suburb' --data @./mappings/suburb_mapping.json
curl -XPUT 'http://127.0.01:9200/accidents/'
curl -XPUT '127.0.01:9200/accidents/_mapping/accident' --data @./mappings/accident_mapping.json
curl -XPUT 'http://127.0.01:9200/suburbs_p/'
curl -XPUT '127.0.01:9200/suburbs_p/location/_mapping' --data @./mappings/suburb_percolator_mapping.json


#source
source LOADER/bin/activate

#load
python ./exercise_data/data-loader.py '127.0.01:9200' 'suburbs'  'suburb' './exercise_data/Melbourne-Localities/melbourne_locality_polygon.shp' 'id' --limit 1000
python ./exercise_data/data-loader.py '127.0.01:9200' 'accidents'  'accident' './exercise_data/melbourne_accident/melbourne_accident.shp' 'id' --limit 50000
python ./exercise_data/data-loader.py '127.0.01:9200' 'suburbs_p'  'suburb' './exercise_data/Melbourne-Localities/melbourne_locality_polygon.shp' 'id' --limit 50000 --createPercolator --percolatorkey 'LOCALITY'
