#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import urllib2
import feedparser
import requests
import config

from storage import CouchDBStorage
from logbook import Logger
from multiprocessing import Pool

log = Logger("system.err")


def getFeeds(url):
    """
    Get the RSS feed of a given URL. The feed is automatically
    downloaded and parsed.
    :param url
    :return
    """
    return feedparser.parse(url)


def getEntries(url):
    """
    Return the list of entries from the feed.
    @return
    """
    return getFeeds(url).get('entries')


def download_entry(feed_entry):
    """
    Download the feed and return it as a string
    :param feed_entry
    :return
    """
    link = feed_entry.get('link')
    req = requests.make_request(config.CHROME, link)

    # Naive download, but works for now.
    data = urllib2.urlopen(req)
    return (feed_entry, data.read())


def main(feed_link, location):
    db = CouchDBStorage(config)
    entries = getEntries(feed_link)

    for entry in entries:
        feed, data = download_entry(entry)
        db.save_mapping(feed, data)


def run(tuple):
    feed_link, location = tuple
    main(feed_link, location)


def _load_links(link_file):
    """Load line separated file which should contain links"""
    with open(link_file, 'r') as fd:
        return [(link, location) for link in fd.readlines()]


def execute(link_file, location):
    pool = Pool(config.POOLSIZE)
    items = _load_links(link_file)

    while True:
        pool.map(run, items)
        time.sleep(config.TIMEOUT)


if __name__ == "__main__":
    import sys
    execute(sys.argv[1], sys.argv[2])
