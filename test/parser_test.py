# *******************************************************************
# !/usr/bin/env python
# -*- coding:utf-8 -*-
# *******************************************************************
# Filename: parser_test.py
# *******************************************************************
# Author: Ioannis Pinakoulakis
# Maintainer: 
# Created: Sun Sep 28 14:29:32 2014 (+0200)
# Version: 
# Last-Updated: 
#           By: 
#     Update #: 0
# Description: 
# *******************************************************************
# Keywords: 
# *******************************************************************
#
__author__ = 'ipinak'

from unittest import TestCase

class BaseParser_Test(TestCase):
    
    def setUp(self):
        self.html_doc = """
        <html><head><title>The Dormouse's story</title></head>
        <body>
        <p class="title"><b>The Dormouse's story</b></p>
        <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.</p>
        
        <div class="entityContainer story">
        <div class="entityMain article">
        <div id='something'>Some text here to make it bigger <b>Bold text here...</b> <a href="http://example.com/link4" class="sister" id="link4">link4</a><br /></div>
        <div class-"Test">Text for class type Test
        <ol><li>Item 1.1</li><li>Item 1.2</li><li>Item 1.3</li></ol>
        <ol><li>Item 2.1</li><li>Item 2.2</li><li>Item 2.3</li></ol>
        </div>
        </div>
        <div class="left">
        <a class="btnLink tag-red" href="/stream/1131/anaskafi-stin-arxaia-amfipoli">ΑΝΑΣΚΑΦΗ ΣΤΗΝ ΑΡΧΑΙΑ ΑΜΦΙΠΟΛΗ</a>
        <a class="btnLink" href="/tag/417/arxaiologia">ΑΡΧΑΙΟΛΟΓΙΑ</a>
        <div class="clear"> </div>
        </div>
        </div>
    
        <div class="after entityCont">Nothing here just testing...</div>
        </body>
        """

    def tearDown(self):
        del self.html_doc


class NaftemporikiParser_Test(BaseParser_Test):

    def test_parse(self):
        from parser import NaftemporikiParser
        np = NaftemporikiParser(self.html_doc)
        parsed_data = np.parse()

        print parsed_data
    
