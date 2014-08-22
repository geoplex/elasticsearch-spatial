# Exercise 1 - Installation

Firstly lets get the initial exercise ready.
```bash
$ cd el-spatial-tutorial
$ git checkout tags/1.0.0
```

OK now we need to create a virtual machine and install Elasticsearch. With vagrant this is easy. However the first time you do this Vagrant needs to do two things:

+ pull down a base machine
+ provision the base machine with Elasticsearch.

so it takes a little longer. To do these things run:
```bash
$ vagrant box add precise32 http://files.vagrantup.com/precise32.box
$ vagrant up
```

During the installation vagrant provisioned the machine with Elasticsearch and some useful plugins:
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
