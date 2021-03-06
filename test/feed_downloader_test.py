# !/usr/bin/env python
# -*- coding:utf-8 -*-
from unittest import TestCase
import tools


__author__ = 'ipinak'


class BaseTest(TestCase):

    def setUp(self):
        self.html_data = """
        <html><head><title>The Dormouse's story</title></head>
        <body>
        <p class="title"><b>The Dormouse's story</b></p>
        <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.</p>

        <div class="entityContainer story">
        <div id='something'>Some text here to make it bigger <b>Bold text here...</b> <a href="http://example.com/link4" class="sister" id="link4">link4</a><br /></div>
        <div class-"Test">Text for class type Test
        <ol><li>Item 1.1</li><li>Item 1.2</li><li>Item 1.3</li></ol>
        <ol><li>Item 2.1</li><li>Item 2.2</li><li>Item 2.3</li></ol>
        </div>
        </div>

        <div class="after entityCont">Nothing here just testing...</div>
        </body>
        """

    def tearDown(self):
        del self.html_data


class Test_FeedDownloader(BaseTest):

    def setUp(self):
        super(Test_FeedDownloader, self).setUp()


    def test_parsing(self):
        '''Pass the html doc and check if it parses and extracts correctly the
        data.'''
        pass


if __name__ == '__main__':
    tools.run_tests(
        [Test_FeedDownloader],
        'reports',
        'unittests - feed_downloader.py test report',
        'General test results'
    )
