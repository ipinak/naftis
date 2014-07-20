#!/usr/bin/env python
# -*- coding:utf-8 -*-
# *******************************************************************
# Author: Ioannis Pinakoulakis
# Created: Sun Sep 28 13:50:26 2014 (+0200)
# Description:
# *******************************************************************
# Keywords: parser, naftemporiki, HTML
# *******************************************************************
# TODO:
# 1) write tests and move stuff to test directory
# *******************************************************************
#
import hashlib
try:
    from bs4 import SoupStrainer, BeautifulSoup
except ImportError:
    print "You need to install beautiful soup"


class BaseParser(object):
    """Base Parser"""

    def parse(self):
        """parse"""
        raise NotImplementedError('Don\'t invoke functions from ' \
                                  + self.__class__.__name__ + ' class.')


class HTMLParser(BaseParser):
    """Base HTML parser"""

    def __init__(self, data):
        BaseParser.__init__(self)
        self.data = data

    def __del__(self):
        del self.data


class NaftemporikiParser(HTMLParser):
    """Parser for naftemporiki.gr RSS"""

    def __init__(self, title, data):
        HTMLParser.__init__(self, data)
        self.title = title

    def parse(self):
        """
        :param data
        :param filter - dictionary with tag attributes and values
        that you want to be considered for filtering
        :returns a dictionary of structure
        {id: 'hash', contents: 'conte', title: 'title'}
        """
        strainer = SoupStrainer(**{'class': 'entityMain article'})
        small_soup = BeautifulSoup(self.data, 'html.parser',
                                   parse_only=strainer)

        def get_keywords():
            base_url = 'http://naftemporiki.gr'
            strainer = SoupStrainer(**{'class': 'left'})
            soup = BeautifulSoup(self.data, 'html.parser',
                                 parse_only=strainer)
            keywords = list()
            for key in soup.find_all('a'):
                if key is not None:
                    keywords.append(
                        {'link': base_url + key['href'],
                         'text': key.contents[0].string}
                    )
            del soup, strainer

            return keywords

        # Create a structure for saving data.
        doc_struct = dict()
        doc_struct['title'] = self.title.encode("ascii", "ignore")
        doc_struct['contents'] = small_soup
        doc_struct['keywords'] = get_keywords()
        doc_struct['id'] = hashlib.sha256(doc_struct['title']).hexdigest()

        # Clean things up, it's python, but still it needs curation
        del small_soup, strainer

        return doc_struct

if __name__ == '__main__':
    import feed_downloader
    feed_link = "http://www.naftemporiki.gr/rssFeed?mode=section&id=1&atype=story"
    for entry in feed_downloader.getEntries(feed_link):
        t, d = feed_downloader.download_entry(entry)
        print "Title: " + t + "\n\n"
        n = NaftemporikiParser(t, d)
        d = n.parse()

        for key, value in d.items():
            print "Key: " + key
            print "Value: " + str(value) + "\n\n"
