#!/usr/bin/env bash

# Update the environment and install helpful tools.
sudo python-software-properties -y
sudo apt-add-repository ppa:ubuntugis/ppa -y
sudo apt-get update
sudo apt-get upgrade gcc -y
sudo apt-get install curl -y
sudo apt-get install vim -y
sudo apt-get install python-dev -y
sudo apt-get install python-virtualenv -y
sudo apt-get install gdal-bin -y
sudo apt-get install git -y
sudo apt-get install unzip -y

# Install a java runtime for elastic search.
sudo apt-get install openjdk-7-jre-headless -y

# Install elastic search and necessary plugins.
mkdir elasticsearch
cd elasticsearch
wget https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.2.2.deb
sudo dpkg -i elasticsearch-1.2.2.deb

# -- Start Elastic Search
sudo update-rc.d elasticsearch defaults 95 10
sudo /etc/init.d/elasticsearch start

# -- Install Elastic Search plugins
sudo /usr/share/elasticsearch/bin/plugin -install mobz/elasticsearch-head
sudo /usr/share/elasticsearch/bin/plugin -install karmi/elasticsearch-paramedic
sudo /usr/share/elasticsearch/bin/plugin -install lukas-vlcek/bigdesk

# Setup Nginx
sudo apt-get install nginx -y 

# Setup Kibana TODO
sudo mkdir /var/www
cd /tmp
wget https://download.elasticsearch.org/kibana/kibana/kibana-3.1.0.tar.gz
tar xzvf kibana-3.1.0.tar.gz
sudo cp -r kibana-3.1.0/* /var/www/
sudo chown -R www-data:www-data /var/www

# Configure nginx
sudo mv /etc/nginx/sites-available/default ~/nginx-default-config
sudo cp /vagrant/provision/config/kibana.nginx-config /etc/nginx/sites-available/kibana
sudo ln -s /etc/nginx/sites-available/kibana /etc/nginx/sites-enabled/kibana
sudo service nginx restart

# Checkout tutorial project
cd ~
git clone https://github.com/geoplex/elasticsearch-spatial.git
cd elasticsearch-spatial

# Install python modules for loading data.
virtualenv LOADER
source LOADER/bin/activate
pip install numpy
pip install cython
pip install fiona
pip install pyes
pip install shapely

# Unzip tutorial data.
cd exercise_data/
unzip Melbourne-Localities.zip
unzip Melbourne_accident.zip
cd ..