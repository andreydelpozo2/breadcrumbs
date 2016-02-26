pip install flask
pip install requests
#pip freeze | grep requests | awk -F'==' '{ print $2 }'

mkdir ${HOME}/local
cd ${HOME}/local
curl https://download.elasticsearch.org/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/2.2.0/elasticsearch-2.2.0.tar.gz | tar -xz
curl https://download.elastic.co/kibana/kibana/kibana-4.4.1-darwin-x64.tar.gz | tar -x