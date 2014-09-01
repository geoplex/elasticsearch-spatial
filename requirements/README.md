# Requirements

To run this tutorial you'll need to install [virtualbox](https://www.virtualbox.org/) and [vagrant](http://www.vagrantup.com/).

I also recommend using the [Sense](https://chrome.google.com/webstore/detail/sense/doinijnbnggojdlcjifpdckfokbbfpbo?hl=en) extension for Chrome which provides a JSON aware interface to Elasticsearch.

Interactions with the Elasticsearch API are illustrated using [cURL](http://curl.haxx.se/)

## Grab the repo
```bash
$ git clone https://github.com/geoplex/elasticsearch-spatial
```
## Python

A python loader is provided in the repositry which helps load shapefiles into Elasticsearch. To use this you'll need python (obviously) and we recommend using virtualenv which can be installed using (assuming you have pip)

```bash
$ pip install virtualenv
```

