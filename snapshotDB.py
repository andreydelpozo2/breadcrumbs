import requests
import os
import json
import datetime

sspath = os.path.join(os.environ['HOME'], 'backup')
data = {'type':'fs','settings':{'location':sspath+'/main','compress':True}}
p = requests.put('http://localhost:9200/_snapshot/main', data=json.dumps(data))
print(p.text)
now = datetime.datetime.now()
p = requests.put('http://localhost:9200/_snapshot/main/'+now.strftime("%d_%m_%Y_%H_%M_%S")+'?wait_for_completion=true')
print(p.text)