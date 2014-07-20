#!/usr/bin/env python
# -*- coding:utf-8 -*-
# *******************************************************************
# Author: Ioannis Pinakoulakis
# Created: Mon Sep  1 22:35:41 2014 (+0200)
# Description:
# *******************************************************************
# TODO:
# 1) add proper spoofing (refactor this mechanism)
# *******************************************************************
# 
import time
import urllib2
import feedparser

from logbook import Logger


log = Logger("system.err")

# Cache structure
# ---------------
# { url: [(date, feed)] }
# -------------------
cache = {} # Keep a cache per url


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
    print feed_entry.keys()
    link = feed_entry.get('link')
    req = urllib2.Request(link)

    # Spoof the request, to make it look like it's from a browser
    # since the stupid guys at naftemporiki.gr think that they can
    # stop someone to not use their info.
    req.add_header(
        "User-Agent",
        "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"
    )
    req.add_header("Method", "GET")

    # Naive download, but works for now.
    data = urllib2.urlopen(req)
    str_data = data.read()
    return (feed_entry.get('title'), str_data)


def save_to_file(title_of_article, contents, location):
    fd = open(u"{0}/{1}.html".format(location, title_of_article[:15]), "w")
    # Try to read the contents, if nothing exists it will raise an exception,
    # then write.
    try:
        fd.read()
    except IOError:
        fd.write(contents)


def main(feed_link, location):
    while True:
        for entry in getEntries(feed_link):
            t, d = download_entry(entry)
            save_to_file(t, d, location)
        time.sleep(3600) # Sleep 15 mins


if __name__ == "__main__":
    pass

