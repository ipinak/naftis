#!/bin/env python
# -*- coding:utf-8 -*-
# ***********************************************************************
# Filename: tools
# ***********************************************************************
# Author: ipinak
# Created: 19/4/14 14:16
# Description: 
# ***********************************************************************
#
__author__ = 'ipinak'

from unittest import makeSuite, TestSuite


def run_tests(test_cases, location='', title=None, description=None):
    import HTMLTestRunner, time
    suite = TestSuite()
    [suite.addTest(makeSuite(tc)) for tc in test_cases]

    timestamp = time.strftime('%Y_%m_%d__%H_%M_%S')
    buffer = file(location + 'TestReport_' + timestamp + '.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=buffer,
                                           title=title,
                                           description=description
    )
    runner.run(suite)
