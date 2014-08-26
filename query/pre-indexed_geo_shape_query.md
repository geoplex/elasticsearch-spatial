# Pre-Indexed Query

Elasticsearch allows us to filter data using a Geo Shape filter.

You can use the Sense plugin to do this. Or CuRL

```bash
curl -XPOST 'http://127.0.01:9200/accidents/_search' -d '{"query": {"filtered": {"query": {"match_all": {} }, "filter": {"geo_shape": {"geometry": {"indexed_shape": {"id": "293", "type": "suburb", "index": "suburbs", "path": "geometry"} } } } } } }' | python -m json.tool
```
