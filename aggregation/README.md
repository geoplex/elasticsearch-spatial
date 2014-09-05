# Geo Distance Aggregation

```bash
curl -XPOST 'http://127.0.01:9200/accidents/_search' -d '{
    "size": 0,
    "aggs": {
        "rings": {
            "geo_distance": {
                "field": "point_location",
                "origin": "144.97959, -37.79845",
                "unit": "m",
                "ranges": [
                    {
                        "to": 100
                    },
                    {
                        "from": 100,
                        "to": 300
                    }
                ]
            }
        }
    }
}'  | python -m json.tool
```

This time with a nested aggregation which breaks each distance bucket down by days

```bash
curl -XPOST 'http://127.0.01:9200/accidents/_search' -d '{
    "size": 0,
    "aggs": {
        "rings": {
            "geo_distance": {
                "field": "point_location",
                "origin": "144.97959, -37.79845",
                "unit": "m",
                "ranges": [
                    {
                        "to": 100
                    },
                    {
                        "from": 100,
                        "to": 300
                    }
                ]
            },
            "aggs": {
                "days": {
                    "terms": {
                        "field": "day_of_w_1"
                    }
                }
            }
        }
    }
}'  | python -m json.tool
```
