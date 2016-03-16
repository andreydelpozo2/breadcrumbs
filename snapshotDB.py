import requests
import os
import json
import datetime
import shutil
import boto3

#make snapshot
allSSBase = os.path.join(os.environ['HOME'], 'backup')
ssLocationName = 'main'
snapShotLocation = os.path.join(allSSBase, ssLocationName)
data = {'type':'fs', 'settings':{'location':snapShotLocation, 'compress':True}}
p = requests.put('http://localhost:9200/_snapshot/'+ssLocationName, data=json.dumps(data))
print(p.text)
now = datetime.datetime.now()
baseName = now.strftime("%d_%m_%Y_%H_%M_%S")
p = requests.put('http://localhost:9200/_snapshot/'+ssLocationName+'/'+baseName+'?wait_for_completion=true')
print(p.text)


##zip backup

zipBackUpPath = shutil.make_archive('/tmp/'+baseName, 'zip', allSSBase, ssLocationName)

#upload to S3
s3 = boto3.resource('s3')
b = s3.Bucket('bc-elastic-bkup')

b.upload_file(zipBackUpPath,baseName)
