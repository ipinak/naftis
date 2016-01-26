#!/usr/bin/env python
# -*- coding:utf-8 -*-
# *******************************************************************
# Author: Ioannis Pinakoulakis
# Created: Mon Sep  1 22:35:41 2014 (+0200)
# Description:
# $ python src/app.py -d tmp -t 10 -l /Users/ipinak/Abstract_Development/Python/naftemporiki_reader/links.txt
# *******************************************************************
#
from naftis import feed_downloader, config
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-l", "--link-file", dest="link",
                  help="file with links to download from")
parser.add_option("-d", "--directory", dest="directory",
                  help="directory to store pages")
parser.add_option("-t", "--timeout", dest="timeout",
                  help="timeout of downloading feeds")
(opts, args) = parser.parse_args()


def set_timeout():
    config.TIMEOUT = opts.timeout


if __name__ == '__main__':
    feed_downloader.execute(opts.link, opts.directory)
