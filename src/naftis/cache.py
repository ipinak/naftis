# !/usr/bin/env python
# -*- coding:utf-8 -*-
# ***************************************************
# Filename: cache.py
# ***************************************************
# Author: Ioannis Pinakoulakis
# Maintainer: 
# Created: Mon Sep  1 10:00:35 2014 (+0200)
# Version: 
# Last-Updated: 
#           By: 
#     Update #: 0
# Description: 
# ***************************************************
# 

class Cache(object):
    '''Abstract object of a cache.'''

    def __init__(self):
        self.cache = dict()
        
    def getElement(self):
        raise NotImplementedError()

    def evict(self):
        raise NotImplementedError()


class LRUCache(Cache):
    def __init__(self, max_size=100):
        '''Create a cache object with Least Recently Used (LRU) semantics, where
        you can specify the maximum size of that cache.'''
        pass

    def getElement(self):
        pass

    def evict(self):
        pass

    def _evictLeastUsedElements(self):
        pass

    def _reorderElements(self):
        pass
