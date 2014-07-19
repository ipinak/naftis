#!/usr/bin/env python

import time
import urllib2
import feedparser

from datetime import datetime
from logbook import Logger



log = Logger("system.err")

# Cache structure
# ---------------
# { url: [(date, feed)] }
# -------------------
cache = {} # Keep a cache per url


def getFeeds(url):
    """
    Get the RSS feed of a given URL. The feed is automatically downloaded and
    parsed.
    @param url
    """
    # tmpDict = { "date": datetime.datetime.now(), "feed": feedparser.parse(url) }
    # if url not in cache:
    #     # Store a tuple
    #     cache[url] = list(tmpDict)
    # else:
    #     tmpL = cache.get(url)
    #     try:
    #         timeDiff = tmpL[-1].get("date") - datetime.datetime.now()
    #         if timeDiff.minute > 15:
    #             tmpL.append(tmpDict)
    #     except IndexError, e:
    #         print "wrong index"
    #         log.error("wrong index in cache for url: {0}".format(url))
    # return cache[url][-1].get("feed")
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
    @param feed_entry
    @return
    """
    print feed_entry.keys()
    link = feed_entry.get('link')
    req = urllib2.Request(link)

    # Spoof the request, to make it look like it's from a browser
    # since the stupid guys at naftemporiki.gr think that they can
    # stop someone to not use their info.
    req.add_header("User-Agent", "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11")
    req.add_header("Method", "GET")

    # Naive download, but works for now.
    data = urllib2.urlopen(req)
    str_data = data.read()
    return (feed_entry.get('title'), str_data)


# TODO: complete this using lxml or libxml2
def retrieve_data(tag, document):
    """
    Retrieve a specific segment of HTML code from a whole document using
    XPath and the given tag
    """
    pass


def save_to_file(title_of_article, contents, location):
    fd = open(u"{0}/{1}.html".format(location, title_of_article[:15]), "wr")
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
    import sys
    if len(sys.argv) < 3:
        print "usage: invalid number of arguments, you must specify feed and where to store data."
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])


