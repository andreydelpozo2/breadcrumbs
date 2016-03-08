import requests
from bs4 import BeautifulSoup
from datetime import datetime
from elasticsearch import Elasticsearch


def count_words_at_url(url):
    resp = requests.get(url)
    return len(resp.text.split())

def simplework(url):
    return url

def indexpage(url):
    try:
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'html.parser')
        soup.get_text()
        es = Elasticsearch()
        es.index(index="bc", doc_type='webpage', body={"timestamp": datetime.now(),"text":soup.get_text(),"url":url})
    except  requests.ConnectionError:
        #log error
        return False

    return True


def dobookmarks(filename):
    soup = BeautifulSoup(file(filename).read(), 'html.parser')
    for anchor in soup.findAll('a', href=True):
        indexpage(anchor['href'])
    return True
