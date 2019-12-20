---
title: "Let's Encrypt and client certificates"
slug: "lets-encrypt-and-client-certificates"
date: "2015-11-25T09:39:00"
categories:
  - Software
tags:
  - SSL
  - security
images:
  - https://letsencrypt.org/certs/isrg-keys.png
  - https://imgs.xkcd.com/comics/security.png
---

A few days ago I switched to [Let's Encrypt][] certificates for this site (instead of StartSSL).

Twitter user [@utopiah][] recently asked me about using it as a <abbr title="Certificate Authority">CA</abbr> to sign
the client certificate instead of using a self-generated, self-signed one.

{{< tweet 664683635354771456 >}}

It's a good question, but the answer needs more than 140 characters :smiley:

There are actually two parts to this question:

* is it possible to use [Let's Encrypt][] to sign client certificates?
* is it better to use such a trusted CA to sign client certificates?

For the first question, the answer is clearly **no**: Let's Encrypt only signs server certificates. It's clear on their
cross-signing schema, and it's also confirmed by the [FAQ][]:

> **Will Let's Encrypt issue certificates for anything other than SSL/TLS for websites?**
>
> Let's Encrypt certificates will be standard Domain Validation certificates, so you can use them for any server that
> uses a domain name, like web servers.

Servers only, validated by domain name: this excludes client certificates.

> **Can I use certificates from Let's Encrypt for code signing or email encryption?**
>
> No. Email encryption and code signing require a different type of certificate than Let's Encrypt will be issuing.

No other usage than servers.

[![Cross-signing schema](https://letsencrypt.org/certs/isrg-keys.png "Cross-signing schema")](https://letsencrypt.org/certificates/)

Now, for the second part: would it be better to use a trusted CA for client certificates? Well, not necessarily. It
depends on the application that's using client certificate authentication.

Specifically, in my case, I use client auth for very simple apps and I am the only authorized user. Thanks to the
private CA, it's extremely simple for the web server to authenticate a connection: if there's a client certificate
signed by the private CA, then the connection is authenticated. Otherwisen there's a [fallback to basic auth][fallback].
And the apps that are protected this way don't even need to check for the login data. They don't even *know* that there
is some form of authentication that protects them :wink:

With a trusted CA, there would be a few extra steps needed: the web server would have to check that the certificate is
valid, signed by the CA, hasn't expired, and hasn't been revoked. (No need for that with the private CA as I'm the only
one issuing certificates). Then it's absolutely necessary to check that the user ID in the client certificate matches a
list of authorized IDs, to prevent other users that have client certificates issued by the same CA from logging in.

To be honest, it's actually probably not a big deal, and I'm sure that it would only take a few lines to configure
lighttpd to do that. But it's still a little bit more complicated than the private CA, for no practical advantage. And
you'd have to completely *trust* the CA, which can sometimes be [complicated][CA compromise].

[![Actual actual reality: nobody cares about his secrets. (Also, I would be hard-pressed to find that wrench for $5)](//imgs.xkcd.com/comics/security.png "XKCD 538")](https://xkcd.com/538/)

[CA compromise]: https://en.wikipedia.org/wiki/Certificate_authority#CA_compromise
[fallback]: /posts/2014/08/13/basic-auth-ssl-client-certificate-dual-method-authentication-in-lighttpd/
[FAQ]: https://Let/t/frequently-asked-questions-faq/26
[Let's Encrypt]: https://letsencrypt.org/
[@utopiah]: https://twitter.com/utopiah
