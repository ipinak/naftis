#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import utils
import couchdb

from datetime import datetime


class FileMapper(object):

    def __init__(self, directory):
        """
        :param directory - directory to store the downloaded code.
        """
        now = datetime.now()
        today = str(now.year) + "_" + str(now.month) + "_" + str(now.day)
        self._directory = directory + "/" + today
        self._create_path()

    @property
    def directory(self):
        return self._directory

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

    def _create_path(self):
        """
        If the path exists return it, otherwise create a path based on
        the current path and the given directory.
        """
        if not os.path.exists(self.directory):
            os.mkdir(self.directory)


class CouchDBStorage(object):

    def __init__(self, config):
        self._config = config
        self.connect()

    def connect(self):
        self._connection = couchdb.Server(self._config.COUCHDB_URL)
        self.db = self._get_db()

    def _get_db(self):
        """Create a new database or get an existig one."""

        db_name = self._config.DB_NAME
        return self._connection[db_name]

    def save_mapping(self, feed, contents):
        """
        Save the contents to the database.
        :param feed
        :param contents
        """
        link = feed.get('link')
        di = {}
        di[link] = unicode(contents, errors='ignore')
        self.db.save(di)
