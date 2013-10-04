#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Thomas Jost'
SITENAME = '/dev/schnouki'
SITEURL = 'http://schnouki.net'

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'

SUMMARY_MAX_LENGTH = None

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "feed.atom"
CATEGORY_FEED_ATOM = "feed.cat-%s.atom"
TAG_FEED_ATOM = "feed.tag-%s.atom"
TRANSLATION_FEED_ATOM = None
FEED_MAX_ITEMS = 10

# Paths
STATIC_PATHS = ['images', 'videos']

# URLs
ARTICLE_URL = 'posts/{date:%Y}/{date:%02m}/{date:%02d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%02m}/{date:%02d}/{slug}/index.html'


# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/Schnouki'),
          ('GitHub', 'http://github.com/Schnouki'),)
TWITTER_USERNAME = "Schnouki"

# Pagination
DEFAULT_PAGINATION = 5

# Theme
THEME="themes/gum"

# Comments
DISQUS_SITENAME = "devschnouki"
