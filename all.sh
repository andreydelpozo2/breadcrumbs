#!/usr/bin/env bash
. ./infrastucture.sh

startInfrastructure
startWorkers
./runserver.sh