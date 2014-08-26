# Delete & Recreate Index

Ok now we want to remove our suburbs index and recreate it, this time using our modified mapping. This will enable us to load the suburb shapefile and Elasticsearch will recognise and index the geometry correctly.

Delete the index
```bash
curl -XDELETE 'http://127.0.01:9200/suburbs'
```
Recreate the index
```bash
curl -XPUT 'http://127.0.01:9200/suburbs/'
```
Add the updated mapping
```bash
curl -XPUT '127.0.01:9200/suburbs/_mapping/suburb' --data @mapping.json
```

Finally load in all the suburbs..
```bash
python data-loader.py '127.0.0.1:9200' 'suburbs'  'suburb' '../exercise_data/Melbourne-Localities/melbourne_locality_polygon.shp' 'id' --limit 1000
```
While the load is running you can monitor the application behaviour by using the head, paramedic or bigdesk plugins.

