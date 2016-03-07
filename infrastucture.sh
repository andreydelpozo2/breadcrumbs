#!/bin/bash

function startInfrastructure()
{
    mydir=${PWD}
    echo ${mydir}
    cd ${HOME}/local
    nohup ./kibana-4.4.1-darwin-x64/bin/kibana -H localhost > kibana.log 2> kibana.err &
    echo $! > ${mydir}/kibara.pid
    nohup ./elasticsearch-2.2.0/bin/elasticsearch > es.log 2> es.err &
    echo $! > ${mydir}/elasticsearch.pid
    nohup ./redis-3.0.7/src/redis-server > redis.log 2> redis.err &
    echo $! > ${mydir}/redis.pid

    #monitor
    nohup rq-dashboard > rqdashboard.log 2> rqdashboard.log &
    echo $! > ${mydir}/rq-dashboard.pid
    cd ${mydir}
}

function stopInfrastructure()
{
    for i in {./kibara.pid,./elasticsearch.pid,./redis.pid,./rq-dashboard.pid}; do
        var=$(<${i})
        kill -6 ${var}
    done
}



#http://localhost:5601/app/sense
#rq-dashboard
#http://0.0.0.0:9181/default