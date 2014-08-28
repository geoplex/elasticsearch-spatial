# Geo Shape Filter

Elasticsearch allows us to filter data using a Geo Shape filter.

You can use the [Sense](https://chrome.google.com/webstore/detail/sense/doinijnbnggojdlcjifpdckfokbbfpbo?hl=en) plugin to do this. Or [cURL](http://curl.haxx.se/)

```bash
curl -XPOST 'http://127.0.01:9200/accidents/_search' -d '{"query": {"filtered": {"query": {"match_all": {} }, "filter": {"geo_shape": {"geometry": {"shape": {"type": "Polygon", "coordinates": [[[144.9400520324707, -37.82158204850761 ], [144.9400520324707, -37.79391457604158 ], [145.0059700012207, -37.79391457604158 ], [145.0059700012207, -37.82158204850761 ], [144.9400520324707, -37.82158204850761 ] ] ] } } } } } } }' | python -m json.tool
```
In the above example we're asking for any accidents which intersect with a basic polygon. This yields 3401 accidents and Elasticsearch took 30ms to process the request.:

```javascript
{
   "took": 30,
   "timed_out": false,
   "_shards": {
      "total": 5,
      "successful": 5,
      "failed": 0
   },
   "hits": {
      "total": 3401,
      "max_score": 1,
      "hits": [....]
    }
}
```
Using this type of filter is useful if you want to pass arbitary geometries to Elasticsearch. For example this filter could be used to return all accidents within the bounding box on a map. Another way of doing this would be to use the [Geo Bounding Box](http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/query-dsl-geo-bounding-box-filter.html) filter
