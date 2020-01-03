#!/usr/bin/env bash
# This script prepare the web server to deploy static content
apt-get -y update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
touch /data/web_static/releases/test/index.html
echo "<html><head><title>Test</title></head><body><h1>Test</h1></body></html>" > /data/web_static/releases/test/index.html
ln -snf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "49i location /hbnb_static/ {" /etc/nginx/sites-available/default
sed -i "50i alias /data/web_static/current/;" /etc/nginx/sites-available/default
sed -i "51i autoindex off;" /etc/nginx/sites-available/default
sed -i "52i }" /etc/nginx/sites-available/default
service nginx restart
