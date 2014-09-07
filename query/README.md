# Exercise 3 - Query

We now have suburb and accident data loaded into our Elasticsearch instance, this exercise will cover the basics of querying data within Elasticsearch, and specifically cover off on the geospatial query features.

There are two ways to search for data in Elasticsearch

* REST Request URI
* REST Request Body

In this exercise we'll be using the REST Request Body method, but for completeness here is an example of a simple query using the REST Request URI method:

```bash
curl 'localhost:9200/accidents/_search?q=pedestrian&pretty'
```

In the above example we're looking for any documents in the accidents index which involve pedestrians. We can run the same query using REST Request Body.

todo - fix this query it doesn't work!

```bash
curl -XPOST  'localhost:9200/accidents/_search' -d '
{
  "query": { "match": "pedestrian" }
}'
```

Now that we've got some basic idea of the query syntax and approach, lets move on to look at some specific geospatial queries.

<todo>

mention the size option to control resultset

talk about how to interpret the response

include some basic information about searching and the query DSL, filters and the differences

maybe use a simple example of term based query

filters perform better
</todo>
