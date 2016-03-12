#!/usr/bin/env bash

sudo cp nginx.default /etc/nginx/sites-available/default
sudo nginx -s reload

