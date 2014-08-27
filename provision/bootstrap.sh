#!/usr/bin/env bash

# Update the environment and install helpful tools.
sudo apt-get update
sudo apt-get install curl -y
sudo apt-get install vim -y

# Install a java runtime for elastic search.
sudo apt-get install openjdk-7-jre-headless -y

# Install python modules.
sudo apt-get install python-virtualenv -y

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

