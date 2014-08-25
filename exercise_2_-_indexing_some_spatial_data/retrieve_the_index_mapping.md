# Retrieve the type Mapping

We now have a single index called 'Suburbs' with a single document loaded into it. Elasticsearch has created a mapping for our suburb type based upon the first document we've loaded in.

To retrieve the mapping:

```bash
curl -s -XGET "http://127.0.0.1:9200/suburbs/suburb/_mapping?pretty=true" > mapping.json
```
You will now have a file called mapping.json which contains the mapping for the suburbs index and suburb type. Open the mapping.json file. Elasticsearch includes the index in the mapping:

```bash
{
  "suburbs" : {
    "mappings" : {...
    }
    }
}
```
The [PUT](http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-put-mapping.html) mapping option on the Elasticsearch API allows you to define a mapping for a specifc type, therefore we need to remove the index definition from the mapping.json file - so remove the above section leaving the suburb type only:

```bash
{
    "suburb": {.....
        }
}
```

You'll notice that Elasticsearch by default has defined the geometry field on the suburb as including a coordinates and type property.

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
We need to update the mapping to tell Elasticsearch that the geometry field is actually a geo shape type. Update the file as follows:

```bash
"geometry" : {
    "type": "geo_shape"
          }
```

