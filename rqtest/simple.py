

from rq import Queue
from redis import Redis
from notworker import count_words_at_url
from notworker import simplework
from notworker import indexpage
import time

# Tell RQ what Redis connection to use
redis_conn = Redis()
q = Queue(connection=redis_conn)  # no args implies the default queue

# Delay execution of count_words_at_url('http://nvie.com')
job = q.enqueue(simplework, 'http://nvie.com')
# Now, wait a while, until the worker is finished
time.sleep(5)
print(job.result)   # => 889