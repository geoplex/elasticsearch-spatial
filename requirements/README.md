# Requirements

To run this tutorial you'll need to install [virtualbox](https://www.virtualbox.org/) and [vagrant](http://www.vagrantup.com/).

I also recommend using the [Sense](https://chrome.google.com/webstore/detail/sense/doinijnbnggojdlcjifpdckfokbbfpbo?hl=en) extension for Chrome which provides a JSON aware interface to Elasticsearch.

Interactions with the Elasticsearch API are illustrated using [cURL](http://curl.haxx.se/)

## Grab the repo
```bash
$ git clone https://github.com/geoplex/elasticsearch-spatial
```
## Python

A python loader is provided in the repositry which helps load shapefiles into Elasticsearch. To use this you'll need python [installed](http://docs.python-guide.org/en/latest/starting/install/osx/).

We recommend using [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/), a tool which provides isolated environments of python.
By using virtualenv you can install python packages without affecting packages installed by other python applications. There is a convenient tool called [virtualevnwrapper](https://pypi.python.org/pypi/virtualenvwrapper) which wraps the functions of virtualenv. i.e., It makes it easier to use virtualenv capabilities.

You can install virtualenv and virtualenvwrapper using [pip](https://pypi.python.org/pypi/pip) (Pip is a tool for easily installing and managing python packages)

*Note:* If you are an osx user, installing python via brew will install and pip.

```bash
$ pip install virtualenv
$ pip install virtualenvwrapper
```

