#!/bin/env python
# -*- coding:utf-8 -*-
import sys
import os
import HTMLTestRunner
import time
from unittest import makeSuite, TestSuite

__author__ = 'ipinak'


def run_tests(test_cases, location='', title=None, description=None):
    suite = TestSuite()
    [suite.addTest(makeSuite(tc)) for tc in test_cases]

    timestamp = time.strftime('%Y_%m_%d__%H_%M_%S')
    filepath = os.getcwd() + "/" + location

    if not os.path.exists(filepath):
        os.mkdir(filepath)
    buffer = file(filepath + '/TestReport_' + timestamp + '.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=buffer,
                                           title=title,
                                           description=description)
    runner.run(suite)


def include_path(*directories):
    """
    Include in the python path one or more directories
    :param directories
    """
    for dir in directories:
        print("> including in python path: " + dir + "\n")
        sys.path.append(dir)


def exclude_path(*directories):
    """
    Exclude from the python path one or more directories
    :param directories
    """
    for dir in directories:
        print("> excluding from python path: " + dir + "\n")
        sys.path.remove(dir)
