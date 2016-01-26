#!/usr/bin/env python
# -*- coding:utf-8 -*-
# *******************************************************************
# Author: Ioannis Pinakoulakis
# Created: Tue Nov 25 00:39:34 2014 (+0100)
# Description:
# *******************************************************************
# TODO:
# 1) add support for CouchDB
# *******************************************************************
#
import utils


class FileMapper(object):

    def __init__(self, directory):
        """
        :param directory - directory to store the downloaded code.
        """
        self.directory = directory

    def save_mapping(self, feed, contents):
        # TODO: change this to provide the data that you want not the feed
        hash_tuple = utils.generate_hash(feed.get('link'))
        self._save_to_file(hash_tuple, contents)

    def _save_to_file(self, hash_tuple, contents):
        fd = open(u'{0}/{1}.html'.format(self.directory, hash_tuple), 'wr')
        # TODO: change this, instead of checking if the file exists
        # try to check if the hash value exists in the file db.
        try:
            fd.read()
        except IOError:
            fd.write(contents)
        finally:
            fd.close()
