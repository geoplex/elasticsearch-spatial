# Insert Into Index

Now that we have our index we can insert a document into it. To do this we're going to use a python loader which is in the loader directory of the repository.

## Set up

Before running the loader - lets make sure we have the dependencies we need.

```bash
$ virtualenv LOADER
$ source LOADER/bin/activate
$ pip install pyes
$ pip install fiona
$ pip install shapely
```

## Load a record

To load a record we'll use the loader - you can find out the parameters expected by the loader using:

```bash
$ python data-loader.py -h
```

To load a single suburb record you can use:

```bash
python data-loader.py '127.0.0.1:9200' 'suburbs'  'suburb' '../exercise_data/Melbourne-Localities/locality_polygon.shp' 'id' --limit 1
```

The --limit optional argument specifies the number of records to load, in this case we only want to load one record.

Now we can test that our record has been loaded into Elasticsearch. Below we ask for the document indexed with the key 0 in the suburbs index.

```bash
$ curl  -s -XGET  http://127.0.0.1:9200/suburbs/suburb/0 | python -m json.tool
```
This will present the json response from Elasticsearch


