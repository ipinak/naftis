#!/usr/bin/env python
# -*- coding:utf-8 -*-
from naftis import feed_downloader, config
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-l",
                  "--link-file",
                  dest="link",
                  help="file with links to download from")
parser.add_option("-d",
                  "--directory",
                  dest="directory",
                  help="directory to store pages")
parser.add_option("-t",
                  "--timeout",
                  dest="timeout",
                  help="timeout of downloading feeds")
(opts, args) = parser.parse_args()


def set_timeout():
    config.TIMEOUT = opts.timeout


if __name__ == '__main__':
    feed_downloader.execute(opts.link, opts.directory)
