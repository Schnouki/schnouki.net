# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = '//schnouki.net'
ABSOLUTE_SITEURL = "http://schnouki.net"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feed.atom"
CATEGORY_FEED_ATOM = "feed.cat-%s.atom"
TAG_FEED_ATOM = "feed.tag-%s.atom"

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing
#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
PIWIK_ENABLED = True

# Flattr
FLATTR_USER = 'Schnouki'
