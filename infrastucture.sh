#!/usr/bin/env bash

function startInfrastructure()
{
    pushd ${HOME}/local

    if [ $(uname) == "Darwin" ]; then
        nohup ./kibana-4.4.1-darwin-x64/bin/kibana -H localhost > kibana.log 2> kibana.err &
    else
        nohup ./kibana-4.4.2-linux-x64/bin/kibana -H localhost > kibana.log 2> kibana.err &
    fi

    echo $! > /tmp/kibara.pid
    nohup ./elasticsearch-2.2.0/bin/elasticsearch > es.log 2> es.err &
    echo $! > /tmp/elasticsearch.pid
    nohup ./redis-3.0.7/src/redis-server > redis.log 2> redis.err &
    echo $! > /tmp/redis.pid

    #monitor
    nohup rq-dashboard > rqdashboard.log 2> rqdashboard.log &
    echo $! > /tmp/rq-dashboard.pid
    popd
}

function stopInfrastructure()
{
    for i in {/tmp/kibara.pid,/tmp/elasticsearch.pid,/tmp/redis.pid,/tmp/rq-dashboard.pid}; do
        var=$(<${i})
        kill -6 ${var}
    done
}


function startWorkers(){
    cd src
    nohup rq worker > ../worker.log 2> ../worker.err &
    echo $! > ../worker.pid
    cd ..
}

function stopWorkers(){
    var=$(<worker.pid)
    kill -2 ${var}
}


#http://localhost:5601/app/sense
#rq-dashboard
#http://0.0.0.0:9181/default
