# Geo Distance Filter

```bash
curl -XPOST 'http://127.0.01:9200/accidents/_search' -d '{
    "query": {
        "filtered": {
            "query": {
                "match_all": {}
            },
            "filter": {
                "geo_distance": {
                    "distance": "1km",
                    "accident.point_location": {
                        "lat": 144.97959,
                        "lon": -37.79845
                    }
                }
            }
        }
    }
}' | python -m json.tool
```

Can we sort by distance?
