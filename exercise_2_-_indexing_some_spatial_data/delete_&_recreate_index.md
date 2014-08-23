# Delete & Recreate Index

Ok now we want to remove our suburbs index and recreate it, this time using our modified mapping. This will enable us to load the suburb shapefile into and Elasticsearch will recognise and index the geometry correctly.

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
curl -XPUT '127.0.01:9200/suburbs/suburb/_mapping' --data @mapping.json
```
