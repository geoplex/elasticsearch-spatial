# Exercise 2 - Indexing

You can think of an <strong>index</strong> in Elasticsearch as a database. Indexes contain <strong>documents</strong> and a document is of a given  <strong>type</strong>. For example we might have an index called 'suburbs' and a type called 'suburb'. The index would contain documents which define suburbs and conform to the type 'suburb'.

In Elasticsearch each index has a <strong>mapping</strong> which is ike a schema definition for all the types within the index.

There's a whole lot more information [here](http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/index.html).

Elasticsearch supports two spatial types <strong>geo point</strong> and <strong>geo shape</strong>. Elasticsearch accepts [GeoJSON](http://geojson.org/) as it's input geometry format. Because our source data is in [Shapefile](http://en.wikipedia.org/wiki/Shapefile) format we need to translate it into GeoJSON so we can insert it into an index. You can think of each record within our source datasets as a document which we'll insert into an Elasticsearch index.

Elasticsearch will automatically create a mapping for a document type when a new document type is indexed. When creating the mapping, Elasticsearch infers the field data types from the document. For example if we have a field called *Name* in our suburb dataset and it contains the suburb name 'Melbourne' then Elasticsearch will infer that the field type for the *Name* field is 'string'. Unfortunately Elasticsearch does not automatically infer the field types for spatial types, to do this we need to manually update the mapping.

In this exercise we're run the following steps using the suburb data:

1. Create a new index.
2. Insert a single document and get Elasticsearch to automatically create the mapping based upon that document.
3. Retrieve the mapping and modify the field type for the geometry.
4. Delete and recreate the index.
5. Insert the modified mapping.
6. Index our suburb data into the index.
7. Run a single script to load the accident data.

At the end of the exercise all the suburb data will be loaded into a new index called 'suburbs' and all the accident data will be loaded into an index called 'accidents'.


