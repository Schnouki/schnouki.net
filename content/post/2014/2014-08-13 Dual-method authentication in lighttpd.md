---
title: "Basic auth / SSL client certificate: dual-method authentication in lighttpd"
slug: "basic-auth-ssl-client-certificate-dual-method-authentication-in-lighttpd"
date: "2014-08-13T09:26:00"
categories:
  - Software
tags:
  - lighttpd
  - lua
  - authentication
  - SSL
  - security
---

On my server I'm running several webapps (such as [Tiny Tiny RSS][tt-rss], [CGP][], and [Shaarli][]). They are all
running on a private, separate subdomain. As I'm the only user, this subdomain is protected at the server-level with
HTTP Basic authentication, and each app is configured to allow full access without requiring any other login.

This works great, is really simple, and has the advantage of being compatible with almost everything (including with the
TT-RSS Android client). But basic auth is still a little annoying in modern browsers: there's an ugly popup, and typing
a very long password several times a day isn't fun. Especially on mobile browsers. So I thought about it, and figured
that a nice solution would be to use SSL client certificates to authenticate myself, with a fallback to standard basic
auth when using a browser that doesn't have the certificate or for legacy applications (such as the TT-RSS Android
client).

But of course such a setup is not supported by [lighttpd][], the HTTP server I'm using:
[SSL client certificates][ssl-client] are handled by the `mod_ssl` module, authentication by the `mod_auth` module, and
they are completely independent, with no way to enable `mod_auth` if the connection wasn't authenticated with a client
certificate.

However basic auth is a really simplistic process, so writing a module that will perform such an authentication is quite
easy: it's just a matter of writing some Lua code and enabling it with [`mod_magnet`][mod_magnet].

So here it is: `comfy-auth.lua`, a nice a comfy authentication method for lighttpd :smiley:

{{< gist Schnouki dee1766f2c7486dbf712 "comfy-auth.lua" >}}

(This script depends on two Lua packages: `mimetypes` and `md5`, which can easily be installed with
[`luarocks`][luarocks]).

I described the configuration I use for SSL client certificates verification [yesterday][ssl-client]; here's what's
needed to add support for comfy auth:

{{< gist Schnouki dee1766f2c7486dbf712 "lighttpd.conf" >}}

The `htdigest` file is generated with this simple shell script:

~~~bash
#!/bin/sh
# Usage: ./hash-digest.sh my_username "My private domain" hunter2 >> /etc/lighttpd/htdigest
user=$1
realm=$2
pass=$3
hash=`echo -n "$user:$realm:$pass" | md5sum | cut -b -32`
echo "$user:$realm:$hash"
~~~

Using this config, I can now authenticate on my private domain using either a client certificate, or simple
basic authentication. And it was fun to do :smiley:


[CGP]: https://github.com/pommi/CGP/
[Shaarli]: http://sebsauvage.net/wiki/doku.php?id=php:shaarli
[lighttpd]: http://www.lighttpd.net/
[luarocks]: http://luarocks.org/
[mod_magnet]: http://redmine.lighttpd.net/projects/lighttpd/wiki/Docs_ModMagnet
[ssl-client]: /posts/2014/08/12/lighttpd-and-ssl-client-certificates/
[tt-rss]: http://tt-rss.org/redmine/projects/tt-rss/wiki
