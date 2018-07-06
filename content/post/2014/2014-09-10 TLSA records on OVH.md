---
title: "TLSA records on OVH"
slug: "tlsa-records-on-ovh"
date: "2014-09-10T11:37:00"
lastmod: "2015-10-09T11:15:00"
categories:
  - Software
tags:
  - dns
  - dnssec
  - security
  - SSL
  - TLSA
---

[DANE][] is a great way of improving security on the web by replacing SSL certificate authorities with DNS records
signed by DNSSEC. Basically, the certificate (or its fingerprint) is contained in a TLSA record, with some paremeters
that specify how clients should validate it.

It is also extremely simple to generate TLSA records for your domain using online tools such as
<https://ssl-tools.net/tlsa-generator> (which, amusingly, is not TLSA-enabled…)

However, if you're hosting your DNS zone on OVH (or any other provider with a version of BIND that does not
support the TLSA RRtype), it gets a little bit more complicated: adding a TLSA record to your zone will make the web
interface complain that this RRtype is unknown.

**EDIT:** OVH now supports TLSA! See the update below.

However it is still possible to add TLSA records to OVH by using a "generic", numeric RRtype. The format however is
quite different. But it can be easily created using the `tlsa` tool included in [hash-slinger][]:

~~~console
$ tlsa --usage 1 --selector 1 --mtype 1 --output generic --certificate /path/to/certificate.pem example.com
_443._tcp.example.com. IN TYPE52 \# 35 0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef012345
~~~

(Be sure to read the tlsa doc to understand what usage, selector and mtype are. Arch Linux users: hash-slinger is now
available on the [AUR][].)

This record can then be added to the zone on OVH without any problem. By the way, my blog is now secured by DANE and
TLSA, as demonstrated by the [DNSSEC/TLSA-Validator][validator] Firefox add-on :smiley:

![TLSA FTW!]({static|/images/2014/tlsa-url.png})

**UPDATE:** OVH now supports records with the TLSA type in its new Manager V6 when editing the zone in text mode. So now
it's possible to use the "RFC" output in `tlsa`:

~~~console
$ tlsa --usage 1 --selector 1 --mtype 1 --output rfc --certificate /path/to/certificate.pem example.com
_443._tcp.example.com. IN TLSA 1 1 1 0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef
~~~

Thanks [@slashdevsda][]!


[AUR]: https://aur.archlinux.org/packages/hash-slinger/
[DANE]: https://en.wikipedia.org/wiki/DNS-based_Authentication_of_Named_Entities
[hash-slinger]: http://people.redhat.com/pwouters/hash-slinger/
[validator]: https://www.dnssec-validator.cz/
[@slashdevsda]: https://twitter.com/slashdevsda
