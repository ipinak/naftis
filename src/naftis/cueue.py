# !/usr/bin/env python
# -*- coding:utf-8 -*-
# ***************************************************
# Filename: cueue.py
# ***************************************************
# Author: Ioannis Pinakoulakis
# Maintainer: 
# Created: Mon Sep  1 21:25:27 2014 (+0200)
# Version: 
# Last-Updated: Mon Sep  1 21:25:31 2014 (+0200)
#           By: Ioannis Pinakoulakis
#     Update #: 1
# Description: 
# ***************************************************
#
import utils


class base_cueue(object):
    def __init__(self, max_size=15):
        self._cache = {}
        self._max_size = max_size

    @property
    def cache(self):
        return self._cache

    @property
    def max_size(self):
        return self._max_size

    def add(self, key, value):
        raise NotImplementedError()

    def remove(self, key):
        raise NotImplementedError()

# TODO: change the cache structure to be like this:
# {
#    {
#      hash_key: feed,
#      date_added: some_date
#    }
# }
class RSScueue(base_cueue):
    def __init__(self, max_size=15):
        base_cueue.__init__(self, max_size)

    @property
    def size(self):
        return len(self.cache.keys())

    def add(self, key, feed):
        hash_key = utils.generate_hash(key)
        self._clear(feed.get('publdate'))
        if len(self.cache.keys()) < self.max_size:
            self.cache[hash_key] = feed

    def remove(self, key):
        '''Remove'''
        hash_key = utils.generate_hash(key)
        return self.cache.get(hash_key)
    
    def _clear(self, date):
        '''Remove entries that have a publish date later than the oldest'''
        if self.size >= self.max_size:
            for key, item in self.cache.items():
                if item.get('publdate') < date and self.size >= self.max_size:
                    del self.cache[key]

    def __str__(self):
        stri = ''
        for k,v in self.cache.items():
            stri = stri + str(k) + ': ' + str(v) + '\n'
        return stri


def stupid_wait():
    for i in xrange(100000):
        pass

if __name__ == '__main__':
    from datetime import datetime
    
    ll = RSScueue()

    fakeRss = [
        {'title': 'title1', 'publdate': datetime.now()},
        {'title': 'title2', 'publdate': datetime.now()},
        {'title': 'title3', 'publdate': datetime.now()},
        {'title': 'title4', 'publdate': datetime.now()}
    ]    
    stupid_wait()
    for f in fakeRss:
        ll.add(f.get('title'), f)

    fakeRss = [
        {'title': 'title5', 'publdate': datetime.now()},
        {'title': 'title6', 'publdate': datetime.now()},
        {'title': 'title7', 'publdate': datetime.now()},
        {'title': 'title8', 'publdate': datetime.now()}
    ]
    stupid_wait()
    for f in fakeRss:
        ll.add(f.get('title'), f)

    fakeRss = [
        {'title': 'title9', 'publdate': datetime.now()},
        {'title': 'title10', 'publdate': datetime.now()},
        {'title': 'title11', 'publdate': datetime.now()}
    ]
    stupid_wait()
    for f in fakeRss:
        ll.add(f.get('title'), f)

    fakeRss = [
        {'title': 'title12', 'publdate': datetime.now()},
        {'title': 'title13', 'publdate': datetime.now()},
        {'title': 'title14', 'publdate': datetime.now()},
        {'title': 'title15', 'publdate': datetime.now()}
    ]
    stupid_wait()
    for f in fakeRss:
        ll.add(f.get('title'), f)
        
    print ll.size

    stupid_wait()
    n1 = {'title': 'title16', 'publdate': datetime.now()}
    ll.add(n1.get('title'), n1)
    
    stupid_wait()
    n2 = {'title': 'title17', 'publdate': datetime.now()}
    ll.add(n2.get('title'), n2)

    stupid_wait()
    n3 = {'title': 'title18', 'publdate': datetime.now()}
    ll.add(n3.get('title'), n3)
    
    n3 = {'title': 'title19', 'publdate': datetime.now()}
    ll.add(n3.get('title'), n3)

    n3 = {'title': 'title20', 'publdate': datetime.now()}
    ll.add(n3.get('title'), n3)

    n3 = {'title': 'title21', 'publdate': datetime.now()}
    ll.add(n3.get('title'), n3)
    
    print ll.size
    print "---------\n"
    print str(ll) + '\n'
