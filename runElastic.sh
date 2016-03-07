#!/bin/bash

cd ${HOME}/local
nohup ./kibana-4.4.1-darwin-x64/bin/kibana -H localhost &
nohup ./elasticsearch-2.2.0/bin/elasticsearch