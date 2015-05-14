#!/usr/bin/env python
# -*- coding:utf-8 -*-
# *******************************************************************
# Author: Ioannis Pinakoulakis
# Created: Tue Nov 25 00:39:34 2014 (+0100)
# Description:
# *******************************************************************
# TODO:
# 1) test the connection to a CouchDB instance
# *******************************************************************
#
#import couchdb
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


class db_connector(object):

    def __init__(self):
        # Log here...
        pass

    def store(self, key, value):
        pass

    def exists(self, key):
        pass

    def delete(self, key):
        pass


class CouchDBConnector(db_connector):

    def __init__(self, server, port):
        self.server = server
        self.port = port

    def connect(self):
        self.couch = couchdb.Server(self.server + ':' + self.port)

    def create(self, document):
        return self.couch.create(document)

    def get(self, cid):
        return self.couch.get(id=cid)

    def save(self, document, data):
        self.couch.save(data)

    def delete(self, data):
        self.couch.delete(data)

    def query(self, map_fn, reduce_fn=None, language='javascript', **options):
        """
        :param options - descending := True | False
        :return
        """
        return self.couch.query(map_fn, reduce_fn, options)


if __name__ == '__main__':
    pass
