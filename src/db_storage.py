#!/bin/env python

import hashlib, sqlite3

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
        Mapper.__init__(self)
        self.db = db
        self.directory = directory

    def save_mapping(self, title):
        hash_tuple = create_mapping(title)
        self._save_to_file(hash_tuple)

    def _save_to_file(self, hash_tuple):
        (hash_v, title_v) = hash_tuple
        fd = open(u'{0}/{1}.html'.format(directory, hash_v), 'wr')
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
    
    def _open(self):
        self.connection = sqlite3.connect(self.db)

    def _close(self):
        self.connection.close()

    def store(self, key, value):
        pass

    def exists(self, key):
        pass

    def delete(self, key):
        pass
    
