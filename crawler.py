#!/usr/bin/env python

import sys
from bs4 import BeautifulSoup

DEFAULT_USER_AGENT='Mozilla/5.0'

def get_raw(url, **kwargs):
    """ kwargs ex.
    extra_headers={'Refer':'somewhere'}
    extra_headers={'User-Agent':'Python'}
    """
    default_headers = {'User-Agent': DEFAULT_USER_AGENT}
    if 'extra_headers' in kwargs:
        default_headers.update(kwargs.get('extra_headers'))
    try:
        stream = urllib2.urlopen(url, headers=default_headeres)
        return stream
    except Exception as get_raw_exception:
        print get_raw_exception
        print 'target_url=%s' % url
        print 'headers=%s' %  default_headers
        raise

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
