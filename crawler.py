#!/usr/bin/env python

import sys
from bs4 import BeautifulSoup

DEFAULT_USER_AGENT='Mozilla/5.0'

def get_raw(url, **kwargs):
    return urllib2.urlopen(url)

def get_soup(url, **kwargs):
    return BeautifulSoup(get_raw(url))

def crawling(url, **kwargs):
    #TODO find target link from url 
    headers = {}
    agent = kwargs.get('agent', None)
    headers.update({'User-Agent':agent or DEFAULT_USER_AGENT})
    
    soup = get_soup(url, **kwargs):


def suckling(url, **kwargs):
    #TODO download target link
    pass

if __name__=='__main__':
    crawling(sys.argv[1])
