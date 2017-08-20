# !/usr/bin/env python
# -*- coding:utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='naftis',
    version='0.1b',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    exclude_package_data={'': ['README.md']}
)
