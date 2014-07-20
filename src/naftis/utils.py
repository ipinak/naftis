# !/usr/bin/env python
# -*- coding:utf-8 -*-
# ***************************************************
# Filename: utils.py
# ***************************************************
# Author: Ioannis Pinakoulakis
# Maintainer: 
# Created: Mon Sep  1 21:23:26 2014 (+0200)
# Version: 
# Last-Updated: Mon Sep  1 22:35:29 2014 (+0200)
#           By: Ioannis Pinakoulakis
#     Update #: 2
# Description: 
# ***************************************************
#
import hashlib

def generate_hash(key):
    '''Generate a tuple containing the given key and it's hash value.'''
    return hashlib.sha224(key).hexdigest()


def convert_to_greeklish(text):
    """
    Generate a text given in greek to english
    """
    pass
