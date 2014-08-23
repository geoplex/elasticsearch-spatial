# Create Index

Lets get started and create our empty index ready for our suburb data.

```bash
$ curl -XPUT 'http://localhost:9200/suburbs/'
```

Elasticsearch should tell you that the index has been created:
```bash
$ {"acknowledged":true}
```

You can also check by using paramedic or head e.g:

http://127.0.0.1:9200/_plugin/head/

