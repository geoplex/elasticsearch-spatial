#!/usr/bin/env bash

#load data script
curl -XPUT 'http://127.0.01:9200/suburbs/'
curl -XPUT '127.0.01:9200/suburbs/_mapping/suburb' --data @../mappings/suburb_mapping.json
curl -XPUT 'http://127.0.01:9200/accidents/'
curl -XPUT '127.0.01:9200/accidents/_mapping/accident' --data @../mappings/accident_mapping.json

# Figureout fiona and shapely dependancies.	
virtualenv LOADER
source LOADER/bin/activate
pip install pyes
pip install fiona
pip install shapely	

#Unzip data
unzip Melbourne-Localities.zip
unzip Melbourne-accident.zip

python data-loader.py '127.0.0.1:9200' 'suburbs'  'suburb' '../exercise_data/Melbourne-Localities/melbourne_locality_polygon.shp' 'id' --limit 1000
python data-loader.py '127.0.0.1:9200' 'accidents'  'accident' '../exercise_data/Melbourne_accident/melbourne_accident.shp' 'id' --limit 50000