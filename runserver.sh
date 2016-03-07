nohup rq worker > worker.log 2> worker.err &
python src/server.py
