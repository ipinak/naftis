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
import hashlib
import sqlite3

NEWS_INSERT = "insert into news_feed values ({0}, {1}, {2}, {3})"

def create_mapping(self, title):
    """
    :returns - a tuple with the hash value and the title
    """
    sha224 = hashlib.sha224(title).hexdigest()
    return (sha224, title)

        
class FileMapper(object):

    def __init__(self, directory, db):
        """
        :param directory - directory to store the downloaded code.
        :param db - filename which stores the hash values.
        """
        self.db = db
        self.directory = directory

    def save_mapping(self, title):
        hash_tuple = create_mapping(title)
        self._save_to_file(hash_tuple)

    def _save_to_file(self, hash_tuple):
        (hash_v, title_v) = hash_tuple
        fd = open(u'{0}/{1}.html'.format(self.directory, hash_v), 'wr')
        # @TODO: change this, instead of checking if the file exists
        # try to check if the hash value exists in the file db.
        try:
            fd.read()
        except IOError:
            fd.write(contents)


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


class SQLiteConnector(db_connector):
    def __init__(self, db):
        """
        :param db - the database filename.
        """
        self.db = db
        self.open()
    
    def open(self):
        self.connection = sqlite3.connect(self.db)

    def close(self):
        self.connection.close()

    def store(self, key, value):
        cursor = self.connection.cursor()
        sql_ins = NEWS_INSERT.format(*value)

        #cursor.execute()

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

    def query(self, map_fn, reduce_fn=None, **options):
        """
        :param options - descending := True | False
        :return
        """
        return self.couch.query(map_fun, reduce_fn, options)


if __name__ == '__main__':
    s = SQLiteConnector('d.d')
    s.store('1', ['title', 'hash', 'filename', 'timestamp'])
