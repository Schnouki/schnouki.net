---
date: "2018-11-23T22:25:38+01:00"
title: "GetSimple CMS with Caddy"
categories:
  - Software
tags:
  - Caddy
---

I just switched my web server from [lighttpd][] to [Caddy][]! No need to write a script to update my [Let's
Encrypt][letsencrypt] certificates, HTTP/2, etc.: pretty nice. But of course I needed to rewrite my configuration.

Most of it was straightforward. I had to delete [some nice things][lighttpd dual-auth], but in the end even that was OK
(I wasn't even using that anymore).

My biggest issue was to get a test site that uses [GetSimple CMS][getsimple] to work with "fancy" URLs (i.e.
`/cms/page_name` instead of `/cms/index.php?id=page_name`). But in the end it worked with that simple snippet:

```
hostname {
	import common  # Snippet for TLS, logging, and security headers
	import php     # Snippet to enable PHP via PHP-FPM
	root /srv/http/hostname/htdocs

	rewrite /cms {
		r ^/(.+)$
		to {path} /cms/?id={1}
	}
}
```

Really simple, but it works!


[Caddy]: https://caddyserver.com/
[getsimple]: http://get-simple.info/
[letsencrypt]: https://letsencrypt.org/
[lighttpd dual-auth]: {{< relref "../2014/2014-08-13 Dual-method authentication in lighttpd.md" >}}
[lighttpd]: https://www.lighttpd.net/
