# Copyright (c) 2014 Thomas Jost
# Based on https://github.com/streeter/pelican-gist/, which is
# Copyright (c) 2013 Chris Streeter
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Extension to Python Markdown to embed Gists from GitHub.

The Gist is normally embedded with some JavaScript, but in case JS is disabled
in the browser, its content is downloaded, highlighted with CodeHilite, and
included in a <noscript> tag.

Basic usage:

    [gist:123456]

Specific filename:

    [gist:123456,file=hello.python]

Specific language for CodeHilite:

    [gist:123456,lang=python]
    [gist:123456,file=hello.py,lang=python

"""

import hashlib
import logging
import os
import os.path

from markdown.extensions import codehilite, Extension
from markdown.inlinepatterns import Pattern
from markdown.util import etree

import requests

logger = logging.getLogger(__name__)
GIST_RE = r"^\[gist:([0-9a-fA-F]+)(?:,file\=([^,\]]+))?(?:,lang\=([^,\]]+))?\]"

class GistPattern(Pattern):
    @property
    def gist_cache(self):
        if hasattr(self, "_gist_cache"):
            return self._gist_cache
        else:
            return None

    @gist_cache.setter
    def gist_cache(self, value):
        self._gist_cache = value
        if value is not None and not os.path.exists(value):
            os.makedirs(value)

    def handleMatch(self, mtch):
        _, gist_id, filename, lang, _ = mtch.groups()
        logger.info("mdx_gist: Found Gist id {}, filename {}, lang {}".format(gist_id, filename, lang))

        # Fetch body (possibly from cache)
        body = self.fetch_gist(gist_id, filename)

        # Create the root element
        elem = etree.Element("div")
        elem.set("class", "gist")

        # Add script element
        script_url = "https://gist.github.com/{}.js".format(gist_id)
        if filename is not None:
            script_url += "?file=" + filename
        script_elem = etree.SubElement(elem, "script")
        script_elem.set("src", script_url)

        # Add body, with lang if defined
        noscript_elem = etree.SubElement(elem, "noscript")
        code = codehilite.CodeHilite(src=body, guess_lang=False, lang=lang, css_class=self.css_class)
        placeholder = self.md.htmlStash.store(code.hilite(), safe=True)
        noscript_elem.text = placeholder

        return elem

    def fetch_gist(self, gist_id, filename=None):
        body = None
        if self.gist_cache is not None:
            body = self.get_cache(gist_id, filename)

        if body is None:
            url = "https://gist.githubusercontent.com/raw/" + gist_id
            msg = "mdx_gist: Downloading Gist " + gist_id
            if filename is not None:
                url += "/" + filename
                msg += ", file " + filename

            resp = requests.get(url)

            if resp.status_code != 200:
                raise Exception("Got status code {} while downloading gist {}".format(resp.status_code, gist_id))
            body = resp.text
            if not body:
                raise Exception("Unable to get the contents of gist {}".format(gist_id))

            if self.gist_cache is not None:
                self.set_cache(gist_id, body, filename)

        return body

    def cache_filename(self, gist_id, filename=None):
        md5 = hashlib.md5()
        md5.update(str(gist_id).encode())
        if filename is not None:
            md5.update(b"\n" + filename.encode())
        return os.path.join(self.gist_cache, "{}.cache".format(md5.hexdigest()))

    def get_cache(self, gist_id, filename=None):
        msg = "mdx_gist: Gist " + gist_id
        if filename is not None:
            msg += ", file " + filename
        cache_file = self.cache_filename(gist_id, filename)
        if not os.path.exists(cache_file):
            logger.info(msg + ": cache miss")
            return None
        logger.info(msg + ": cache hit")
        with open(cache_file, "rb") as cache:
            return cache.read().decode()

    def set_cache(self, gist_id, body, filename=None):
        msg = "mdx_gist: Gist " + gist_id
        if filename is not None:
            msg += ", file " + filename
        with open(self.cache_filename(gist_id, filename), "wb") as cache:
            cache.write(body.encode())
        logger.info(msg + ": added to cache")

class GistExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        pattern = GistPattern(GIST_RE)
        pattern.gist_cache = self.config.get("cache", None)
        pattern.css_class = self.config.get("css_class", "codehilite")
        pattern.md = md
        md.inlinePatterns.add("gist", pattern, "_end")
