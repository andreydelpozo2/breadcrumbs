import requests
from bs4 import BeautifulSoup
from datetime import datetime
from elasticsearch import Elasticsearch


def count_words_at_url(url):
    resp = requests.get(url)
    return len(resp.text.split())

def simplework(url):
    return url

def indexpage_off(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    soup.get_text()
    es = Elasticsearch()
    es.index(index="bc", doc_type='webpage', body={"timestamp": datetime.now(),"text":soup.get_text(),"url":url})
    return True
