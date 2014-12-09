# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import sys
sys.path.append(os.curdir)

AUTHOR = "Thomas Jost"
SITENAME = "/dev/schnouki"
SITEURL = ""
SITE_DESCRIPTION = "A blog about emacs, Linux, and other things that I care about."
ABSOLUTE_SITEURL = "http://schnouki.net"

LANDING_PAGE_ABOUT = {
    "title": "/dev/schnouki",
    "details": """Hi there! I'm Thomas Jost, aka "Schnouki". I'm a French software engineer,
    currently working at <a href="http://www.findspire.com/">Findspire</a>, and
    this is my personal blog.<br/>
    <small><a href="/pages/about-me.html">↪ Details</a></small>"""
}

PROJECTS = [
    {
        "name": "spop",
        "url": "https://github.com/Schnouki/spop/",
        "description": "A Spotify client running as a daemon, similar to mpd.",
    }, {
        "name": "git-annex-remote-hubic",
        "url": "https://github.com/Schnouki/git-annex-remote-hubic",
        "description": "A git-annex special remote for hubiC",
    }, {
        "name": "git-annex-zsh-completion",
        "url": "https://github.com/Schnouki/git-annex-zsh-completion",
        "description": "zsh completion for git-annex",
    }, {
        "name": "bccc",
        "url": "https://github.com/Schnouki/bccc",
        "description": "buddycloud console client",
    }, {
        "name": "pympress",
        "url": "https://github.com/Schnouki/pympress",
        "description": "A simple dual-screen PDF reader designed for presentations",
    }
]

SITE_LICENSE = """
<a rel="license" href="//creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="//i.creativecommons.org/l/by-sa/4.0/80x15.png"/></a>
<span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">/dev/schnouki</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="//schnouki.net/" property="cc:attributionName" rel="cc:attributionURL">Thomas Jost</a> is licensed under a <a rel="license" href="//creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
"""

TIMEZONE = "Europe/Paris"
DEFAULT_LANG = "en"
LOCALE = "en_US"
DEFAULT_DATE_FORMAT = "%Y-%m-%d"

SUMMARY_MAX_LENGTH = None

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
AUTHOR_FEED_ATOM = AUTHOR_FEED_RSS = None
TAG_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
FEED_MAX_ITEMS = 10

# Paths
STATIC_PATHS = ["files", "images", "videos", ".well-known"]

# URLs
ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"

# Blogroll
# LINKS =  (('Pelican', 'http://getpelican.com/'),
#           ('Python.org', 'http://python.org/'),
#           ('Jinja2', 'http://jinja.pocoo.org/'),
#           ('You can modify those links in your config file', '#'),)

# Social widget
GITHUB_URL = "http://github.com/Schnouki"
GOOGLEPLUS_URL = GOOGLE_PLUS_PROFILE_URL = "https://plus.google.com/114147327713811044331"
TWITTER_USERNAME = "Schnouki"
TWITTER_URL = "http://twitter.com/" + TWITTER_USERNAME
SOCIAL_PROFILE_LABEL = "Stay in touch"
SOCIAL = (
    ("Email", "mailto:%73%63%68%6E%6F%75%6B%69%2B%62%6C%6F%67%40%73%63%68%6E%6F%75%6B%69%2E%6E%65%74"),
    ("Twitter", TWITTER_URL),
    ("Google+", GOOGLEPLUS_URL, "google-plus"),
    ("GitHub", GITHUB_URL),
    ("StackOverflow", "http://stackoverflow.com/users/113325/schnouki", "stack-overflow"),
    ("LinkedIn", "http://fr.linkedin.com/in/thomasjost/"),
    ("RSS", "/feed.atom"),
)

# Pagination
DEFAULT_PAGINATION = 5

# Theme
THEME = "themes/elegant"
DIRECT_TEMPLATES = (("index", "tags", "categories", "archives",
                     "search", "404"))

# Comments
DISQUS_SITENAME = "devschnouki"
DISQUS_CATEGORY_ID = "3080209"  # Dev

# WOT verification
WOT_VERIFICATION = "e25aa11fbca7a793ac6d"

# Tags
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100

# Plugins
# pip install --user pelican-autostatic webassets yuicompressor
PLUGIN_PATHS = ["my_plugins", "plugins"]
PLUGINS = ["autostatic",
           "my_sitemap", "my_share_post",
           "extract_toc", "neighbors", "related_posts", "summary",
           "tipue_search"]

SITEMAP = {"format": "xml"}

# Markdown extensions
# pip install --user mdx_del_ins beautifulsoup4
from mdx_del_ins import DelInsExtension
from my_plugins import mdx_emojis, mdx_gist
MD_EXTENSIONS = ["codehilite(css_class=highlight)", "extra", "headerid", "toc",
                 DelInsExtension(),
                 mdx_emojis.EmojifyExtension(),
                 mdx_gist.GistExtension(cache="cache/gist", css_class="highlight")]
