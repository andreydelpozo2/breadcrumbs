import requests
r = requests.post('http://127.0.0.1:5000/addmore',data={'param2':'https://wiki.unrealengine.com/Git_source_control_(Tutorial)'})
r.text
