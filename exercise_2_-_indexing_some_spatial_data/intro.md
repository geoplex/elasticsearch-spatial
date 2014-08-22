# Intro

Basically you can think of an <strong>index</strong> in Elasticsearch as a database. Indexes contain <strong>documents</strong> and a document is of a given  <strong>type</strong>. For example we might have an index called 'suburbs' and a type called 'suburb'. The index would contain documents which define suburbs and conform to the type 'suburb'.

In Elasticsearch each index has a <strong>mapping</strong> which is ike a schema definition for all the types within the index.

There's a whole lot more information [here](http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/index.html).

Elasticsearch supports two spatial types <strong>geo point</strong> and <strong>geo shape</strong>. Elasticsearch accepts GeoJSON as it's input geometry format. Therefore we need to translate our source data into GeoJSON so we can insert our data into an index. You can think of each record within our source datasets as a document which we'll insert into an Elasticsearch index.

Elasticsearch will automatically create a mapping for a document type when a new document type is indexed. When creating the mapping, Elasticsearch infers the field data types from the document. For example if we have a field called 'Name' in our suburb dataset and it contains the suburb name 'Melbourne' then Elasticsearch will infer that the field type for the Name field is 'string'. Unfortunately Elasticsearch does not automatically infer the spatial types. In this exercise we're going to do the following:

1. Create the index
2. Insert a single document and get Elasticsearch to automatically create the mapping
3. Retrieve the mapping and modify the field type for the geometry
4. Delete and recreate the index
5. Insert the modified mapping
6. Index our data.
