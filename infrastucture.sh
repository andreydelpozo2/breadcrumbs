#!/bin/bash

cd ${HOME}/local
nohup ./kibana-4.4.1-darwin-x64/bin/kibana -H localhost > kibana.log 2> kibana.err &
nohup ./elasticsearch-2.2.0/bin/elasticsearch > es.log 2> es.err &
nohup ./redis-3.0.7/src/redis-server > redis.log 2> redis.err &

#monitor 
nohup rq-dashboard > rqdashboard.log 2> rqdashboard.log &


#http://localhost:5601/app/sense
#rq-dashboard
#http://0.0.0.0:9181/default