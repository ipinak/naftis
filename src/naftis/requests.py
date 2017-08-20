# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ipinak'

import urllib2
import config


UA = 'User-Agent'


class FirefoxSpoofedRequest(urllib2.Request):

    def __init__(self, *args, **kwargs):
        urllib2.Request.__init__(self, *args, **kwargs)
        self.add_header(UA, config.FIREFOX)


class SafariSpoofedRequest(urllib2.Request):

    def __init__(self, *args, **kwargs):
        urllib2.Request.__init__(self, *args, **kwargs)
        self.add_header(UA, config.SAFARI)


class IESpoofedRequest(urllib2.Request):

    def __init__(self, *args, **kwargs):
        urllib2.Request.__init__(self, *args, **kwargs)
        self.add_header(UA, config.IE)


class ChromeSpoofedRequest(urllib2.Request):

    def __init__(self, *args, **kwargs):
        urllib2.Request.__init__(self, *args, **kwargs)
        self.add_header(UA, config.CHROME)


class RequestProxy(urllib2.Request):
    """The proxy's purpose is to spoof the header with another User-Agent"""

    def __init__(self, ua_type, *args, **kwargs):
        urllib2.Request.__init__(self, *args, **kwargs)
        self.add_header(UA, ua_type)


def make_request(ua_type, *args, **kwargs):
    """
    Given a User-Agent type it creates a spoofed request using
    `urllib2.Request`, for information about the acceptable user agents
    check `config.py`.
    :param ua_type: the user agent to spoof the request
    :param args: arguments for `urllib2.Request`
    :param kwargs: named arguments for `urllib2.Request`
    """

    acceptable_uas = [config.CHROME, config.IE, config.FIREFOX, config.SAFARI]
    if ua_type not in acceptable_uas:
        print("*** Error: given ua_type is not acceptable; check config.py")
        return
    return RequestProxy(ua_type, *args, **kwargs)
