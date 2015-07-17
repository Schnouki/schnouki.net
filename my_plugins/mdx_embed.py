# Copyright (C) 2015 Thomas Jost
# Loosely based on  https://github.com/josh146/embedly_cards, which is
# Copyright (C) 2014 Joshua Izaac
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>

import logging

from markdown.inlinepatterns import Pattern
from markdown.extensions import Extension

logger = logging.getLogger(__name__)

EMBED_RE = r"\[!embedly(?:\?(?P<params>.*))?\]\((?P<url>.+)\)"

class EmbedlyPattern(Pattern):
    def handleMatch(self, mtch):
        url = mtch.group("url")
        params = mtch.group("params")
        logger.info("mdx_embed: Found URL {url}, params: {params}".format(url=url, params=params))

        if params:
            params = {key: value for key, value in [param.split("&") for param in params.split("&")]}
        else:
            params = {}

        link = '<a class="embedly-card"'
        for key, value in params:
            if key != "title":
                link += ' data-card-{key}="{value}"'.format(key=key, value=value)
        link += ' href="{url}">{title}</a>'.format(url=url, title=params.get("title", ""))

        return self.md.htmlStash.store(link)


class EmbedlyExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        pattern = EmbedlyPattern(EMBED_RE)
        pattern.md = md
        md.inlinePatterns.add("embedly", pattern, "_begin")
