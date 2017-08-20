#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import utils

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

    def connect(self):
        self._username = self._config.get("db_username")
        self._password = self._config.get("db_password")

        # Create the connection here
        # self._connection = CouchDB()

    def save(self, hash, contents):
        """
        Save the contents to the database.
        :param hash
        :param contents
        """
        pass
