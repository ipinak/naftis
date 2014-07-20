# !/usr/bin/env python
# -*- coding:utf-8 -*-
# ***************************************************
# Filename: setup.py
# ***************************************************
# Author: Ioannis Pinakoulakis
# Maintainer: 
# Created: Mon Sep  1 19:31:12 2014 (+0200)
# Version: 
# Last-Updated: 
#           By: 
#     Update #: 0
# Description: 
# ***************************************************
#
from setuptools import setup, find_packages

setup(
    name = 'naftis',
    version = '0.1b',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    exclude_package_data = { '': ['README.md'] }
)
