#!/usr/bin/env bash
pip install -r requirements.txt
#pip freeze | grep requests | awk -F'==' '{ print $2 }'

aa=$(uname)

#install elastic search and kinaba
mkdir ${HOME}/local
cd ${HOME}/local
curl https://download.elasticsearch.org/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/2.2.0/elasticsearch-2.2.0.tar.gz | tar -xz
if [ ${aa} == "Darwin" ]; then
    curl https://download.elastic.co/kibana/kibana/kibana-4.4.1-darwin-x64.tar.gz | tar -xz
    ./kibana-3.4.1-darwin-x64/bin/kibana plugin --install elastic/sense
else
    curl https://download.elastic.co/kibana/kibana/kibana-4.4.2-linux-x64.tar.gz  | tar -xz
    ./kibana-4.4.2-linux-x64/bin/kibana plugin --install elastic/sense
fi

cp ./deploy/elasticsearch.yml ${HONE}/local/elasticsearch-2.2.0/config/elasticsearch.yml

cd ${HOME}/local

wget http://download.redis.io/releases/redis-3.0.7.tar.gz
tar xzf redis-3.0.7.tar.gz
cd redis-3.0.7
make
