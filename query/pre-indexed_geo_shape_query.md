# Pre-Indexed Query

Elasticsearch allows us to filter data using a Geo Shape filter.

You can use the [Sense](https://chrome.google.com/webstore/detail/sense/doinijnbnggojdlcjifpdckfokbbfpbo?hl=en) plugin to do this. Or [cURL](http://curl.haxx.se/)

```bash
curl -XPOST 'http://127.0.01:9200/accidents/_search' -d '{"query": {"filtered": {"query": {"match_all": {} }, "filter": {"geo_shape": {"geometry": {"indexed_shape": {"id": "293", "type": "suburb", "index": "suburbs", "path": "geometry"} } } } } } }' | python -m json.tool
```
In the above example we're asking for any accidents which intersect with a suburb with the id 293. This yields:

```javascript
{
   "took": 17,
   "timed_out": false,
   "_shards": {
      "total": 5,
      "successful": 5,
      "failed": 0
   },
   "hits": {
      "total": 413,
      "max_score": 1,
      "hits": [....]
    }
}
```

