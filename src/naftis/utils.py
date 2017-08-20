# !/usr/bin/env python
# -*- coding:utf-8 -*-
import hashlib


def generate_hash(key):
    '''Generate a tuple containing the given key and it's hash value.'''
    return hashlib.sha224(key).hexdigest()


def convert_to_greeklish(text):
    """
    Generate a text given in greek to english
    """
    pass
