#!/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'ipinak'

import tools, unittest

#########################################################################
### Internal functions
#########################################################################
def log_tc(fn):
    def wrapped(*args, **kwargs):
        tc_instance = args[0]
        retVal = 'error'
        print '\n### Starting TC: ' + fn.__name__
        try:
            retVal = fn(*args, **kwargs)
            print retVal
        except Exception, e:
            tc_instance.fail(e.message)
        print '### Log output: ' + str(retVal)
    return wrapped


class SQLiteConnector_Test(unittest.TestCase):
    def setUp(self):
        self.db_storage = db_storage.SQLiteConnector('tmp.db')

    def test_store(self):
        self.db_storage.store('id', ['title', 'hash', 'filename', 'timestamp'])


if __name__ == '__main__':
    tools.run_tests(
        [SQLiteConnector_Test],
        'test/reports/',
        'Unittest - db_storage.py test report',
        "General test results"
    )
