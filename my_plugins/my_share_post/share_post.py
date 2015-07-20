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
    main_title = BeautifulSoup(content.title, 'html.parser').get_text().strip()
    sub_title = ''
    if hasattr(content, 'subtitle'):
        sub_title = ' ' + BeautifulSoup(content.subtitle, 'html.parser').get_text().strip()
    return quote(('%s%s' % (main_title, sub_title)).encode('utf-8'))


def article_url(content, campaign=None):
    site_url = content.settings['ABSOLUTE_SITEURL']
    if campaign is not None:
        campaign = "#pk_campaign=" + campaign
    return quote(('%s/%s%s' % (site_url, content.url, campaign)).encode('utf-8'))


def share_post(content):
    if isinstance(content, contents.Static):
        return
    title = article_title(content)
    _url = lambda cp: article_url(content, "share_" + cp)

    tweet = ('%s%s%s' % (title, quote(' '), _url("tw"))).encode('utf-8')
    diaspora_link = 'https://sharetodiaspora.github.io/?title=%s&url=%s' % (title, _url("diasp"))
    facebook_link = 'http://www.facebook.com/sharer/sharer.php?s=100&amp;p%%5Burl%%5D=%s' % _url("fb")
    gplus_link = 'https://plus.google.com/share?url=%s' % _url("gplus")
    twitter_link = 'http://twitter.com/home?status=%s' % tweet
    linkedin_link = 'https://www.linkedin.com/shareArticle?mini=true&url=%s&title=%s&source=%s' % (
        _url("li"), title, _url("li")
    )

    mail_link = 'mailto:?subject=%s&amp;body=%s' % (title, _url("mail"))

    share_links = {
                   'diaspora': diaspora_link,
                   'twitter': twitter_link,
                   'facebook': facebook_link,
                   'google-plus': gplus_link,
                   'linkedin': linkedin_link,
                   'email': mail_link
                   }
    content.share_post = share_links


def register():
    signals.content_object_init.connect(share_post)
