# Retrieve the Index Mapping

We now have a single index called 'Suburbs' with a single document loaded into it. Elasticsearch has created a mapping for our suburb type based upon the first document we've loaded in.

To retrieve the mapping:

```bash
curl -s -XGET "http://127.0.0.1:9200/suburbs/suburb/_mapping?pretty=true" > mapping.json
```
You will now have a file called mapping.json which contains the mapping for the suburb type. Open the mapping.json file. You'll notice that Elasticsearch by default has defined the coordinates field on the geometry as a double.

```bash
"geometry" : {
            "properties" : {
              "coordinates" : {
                "type" : "double"
              },
              "type" : {
                "type" : "string"
              }
            }
          }
```
We need to update the mapping to tell Elasticsearch that the coordinates field is actually a geo shape type. Update the file as follows:

```bash
"geometry" : {
    "type": "geo_shape"
          }
```

