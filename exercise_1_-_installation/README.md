# Exercise 1 - Installation

Firstly lets get the initial exercise ready.
```bash
$ cd el-spatial-tutorial
```

OK now we need to create a virtual machine and install Elasticsearch. With vagrant this is easy. The vagrant script provided with this tutorial uses a base box named *precise32*. Vagrant box is a pre-packaged environment. However the first time you do this Vagrant needs to do two things:

+ pull down a base machine (i.e., [vagrant box](https://docs.vagrantup.com/v2/boxes.html))
+ provision the base machine with Elasticsearch.

so it takes a little longer. To do these things run:
```bash
$ vagrant box add precise32 http://files.vagrantup.com/precise32.box
$ vagrant up
```

During the installation vagrant provisions the machine with Elasticsearch, Kibana and some useful plugins:
+ [Paramedic](https://github.com/karmi/elasticsearch-paramedic)
+ [Head](http://mobz.github.io/elasticsearch-head/)
+ [BigDesk](https://github.com/lukas-vlcek/bigdesk)

Vagrant also sets up some port forwarding which allows us to access the machine using ssh as well as the Elasticsearch API.

If you want to ssh to the machine you can run:
```bash
$ vagrant ssh
```

Paramedic, Head and BigDesk should be accessible by accessing the following URL's:

+ http://127.0.0.1:9200/_plugin/paramedic/
+ http://127.0.0.1:9200/_plugin/head/
+ http://127.0.0.1:9200/_plugin/bigdesk/
