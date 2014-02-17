#!/usr/bin/env python

import sys
from bs4 import BeautifulSoup

def get_raw(url):
    return urllib2.urlopen(url)

def get_soup(url):
    return BeautifulSoup(get_raw(url))

def crawling(url, **kwargs):
    #TODO find target link from url 
    pass    

def suckling(url, **kwargs):
    #TODO download target link
    pass

if __name__=='__main__':
    crawling(sys.argv[1])
