"""
Share Post
==========

This plugin adds share URL to article. These links are textual which means no
online tracking of your readers.
"""

from bs4 import BeautifulSoup
try:
    from urllib.parse import quote
except ImportError:
    from urllib import quote
from pelican import signals, contents


def article_title(content):
    main_title = BeautifulSoup(content.title, 'html.parser').prettify().strip()
    sub_title = ''
    if hasattr(content, 'subtitle'):
        sub_title = BeautifulSoup(content.subtitle, 'html.parser').prettify().strip()
    return quote(('%s %s' % (main_title, sub_title)).encode('utf-8'))


def article_url(content, campaign=None):
    site_url = content.settings['ABSOLUTE_SITEURL']
    if campaign is not None:
        campaign = "#pk_campaign=" + campaign
    return quote(('%s/%s%s' % (site_url, content.url, campaign)).encode('utf-8'))


def article_summary(content):
    return quote(content.summary.encode('utf-8'))


def share_post(content):
    if isinstance(content, contents.Static):
        return
    title = article_title(content)
    summary = article_summary(content)

    facebook_url = article_url(content, "share_fb")
    gplus_url = article_url(content, "share_gplus")
    twitter_url = article_url(content, "share_tw")
    mail_url = article_url(content, "share_mail")

    tweet = '%s %s' % (title, twitter_url)
    facebook_link = 'http://www.facebook.com/sharer/sharer.php?s=100' \
                    '&p[url]=%s&p[images][0]=&p[title]=%s&p[summary]=%s' \
                    % (facebook_url, title, summary)
    gplus_link = 'https://plus.google.com/share?url=%s' % gplus_url
    twitter_link = 'http://twitter.com/home?status=%s' % tweet
    mail_link = 'mailto:?subject=%s&body=%s' % (title, mail_url)

    share_links = {'twitter': twitter_link,
                   'facebook': facebook_link,
                   'google-plus': gplus_link,
                   'email': mail_link
                   }
    content.share_post = share_links


def register():
    signals.content_object_init.connect(share_post)
