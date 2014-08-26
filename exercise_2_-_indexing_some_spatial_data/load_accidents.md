# Load Accidents

Now we've ran through each of the individual steps to load suburb information yoi can execute the below script to run accidents in to a new index.

Create new accident index and load in pre-configured accident mapping.
```bash
curl -XPUT 'http://127.0.01:9200/accidents/'
curl -XPUT '127.0.01:9200/accidents/_mapping/accident' --data @accident_mapping.json
```

Load in the accident data using the python data loader (remember to configure your virtualenv if you've haven't done so already)
```bash
python data-loader.py '127.0.0.1:9200' 'accidents'  'accident' '../exercise_data/Melbourne_accident/melbourne_accident.shp' 'id' --limit 50000
```
