# Pre-Indexed Query

Elasticsearch also provides a feature whereby indexed spatial data can be used as a filter.

```bash
curl -XPOST 'http://127.0.01:9200/accidents/_search' -d '{
    "query": {
        "filtered": {
            "query": {
                "match_all": {}
            },
            "filter": {
                "geo_shape": {
                    "geometry": {
                        "indexed_shape": {
                            "id": "293",
                            "type": "suburb",
                            "index": "suburbs",
                            "path": "geometry"
                        }
                    }
                }
            }
        }
    }
}' | python -m json.tool
```
In the above example we're asking for any accidents which intersect with a pre-indexed   suburb with the id 293. This yields:

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

