import requests
r = requests.post('http://127.0.0.1:5000/addmore',data={'param2':'http://www.google.com/about'})
r.text
