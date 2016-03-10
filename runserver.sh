#!/usr/bin/env bash

if [ "$1" == "prod" ]; then
	uwsgi --chdir src  -s /tmp/uwsgi.sock -w server:app --chmod-socket=666
else
	python src/server.py
fi