---
date: 2018-12-14
title: "Open Source software"
weight: 201401
---

I've contributed to Open Source / Free Software projects for more than a decade. I've also started a few projects; most
of that is available on my [GitHub page][].

<!--more-->

I'm a self-taught developer. My first programming experiments were made with [QBasic][] (from the Windows 95 CD-Rom…),
then [Turbo Pascal][], then C and C++, and later Python, Java, JavaScript, etc.

I got interested in Linux and Free Software around 2003. I quickly started to submit issues on bug trackers, write or
translate documentation and manual pages, and take part in various forums and mailing lists. In 2006, after I joined
[Supélec][] as a student in engineering, I started being more active and submitting patches to various projects.

Since then I contributed to *many* projects. Here's an incomplete list…


## Projects I created

- **[spop][]**: a headless Spotify client based on the now deprecated `libspotify`, similar in functionality to [MPD][].
  Written in plain C. Spop has been used in [many](https://imgur.com/a/aGjPB) [very](https://imgur.com/gallery/B0zdO)
  [cool](https://volumio.org/) [projects](http://www.runeaudio.com/).
- **[Pympress][]**: a simple yet powerful PDF reader designed for dual-screen presentations. Written in Python; now
  maintained by [@Cimbali][].
- [Caddyfile-mode][]: an Emacs major mode to edit configuration files for the [Caddy web server][]. Written in Emacs
  Lisp.
- [islas][]: a command-line tool to quickly get timetables for the public transporation system Réseau Stan in Nancy,
  France. Written in Go. See the [announcement post]({{< relref "/post/2018/2018-08-25 islas.md" >}}) (in French).
- [git-annex-remote-hubic][]: a "special remote" for [git-annex][] that allows to store content in [hubiC][]. Written in
  Python.
- [hugo-baguetteBox][]: a "theme component" to easily integrate the [baguetteBox.js][] gallery with the [Hugo][] static
website generator (used on this blog).


## Projects I forked

- [ZSH completion for git-annex][]


## Code contributions

- **[ImageMagick][]**: a program and library to create, edit, compose, convert and apply many effects to bitmap images.
  Fixed a cleanup/initialization issue that affected Emacs and many other programs that depended on ImageMagick.
- **[youtube-dl][]**: command-line program to download videos from YouTube and other video sites. Added support for 2
  more sites.
- **[Hugo][]**: fast and flexible static site generator (used on this blog). Fixed a bug that prevented tags (or other
  "taxonomy fields") to be fully lower-case.
- [sorl-thumbnail][]: thumbnails for Django. Fixed a few bugs and reworked the Travis configuration so that all the
  tests would pass again :wink:
- [django-modeltranslation][]: translate Django models. Fixed an issue that prevented that library to work with Django
  1.10+ when using abstract models with custom managers.
- [devd][]: a local web server for developers. Added a small but useful feature: sort the directory listing content by
  file name.
- [collectd][]: the system statistics collection daemon. Fixed the Chrony (NTP server) module.
- [glib][]: core application building blocks for libraries and applications written in C. Submitted a patch for
  `gdbus-codegen`, a tool that generates DBus bindings from a DBus XML schema, to add support for the
  `Property.EmitsChangedSignal` annotation (which was needed by spop). It took 6 years and a migration from Bugzilla to
  GitLab for this patch to be merged :smile: ([original issue](https://bugzilla.gnome.org/show_bug.cgi?id=674913),
  [final merge request](https://gitlab.gnome.org/GNOME/glib/merge_requests/532)).
- [raven-go](https://github.com/Schnouki/raven-go): Sentry client in Go. Submitted a Pull Request to make reported stack
  traces more useful in environments with different build and runtime locations, such as Heroku. Not merged yet.
- [healthchecks.io][]: a Cron Monitoring Tool written in Python & Django. Added support for the [PushOver][] service for
  push notifications.
- [django-weasyprint][]: Django class-based view generating PDF resposes using WeasyPrint. Added a feature that makes it
  faster and safer when building PDFs that should only use local images, stylesheets and fonts.
- (plus all my contributions to [Buddycloud]({{< relref "buddycloud" >}}).)


## Other contributions

- **This blog!** Most of what I write is about software. The two most popular posts ([Flashing a stock Android image
  without wiping user data][post:android] and [OpenVPN for a single application on Linux][post:openvpn]) are linked from
  multiple sites, forums and other blogs, and have hundreds of monthly readers.
- I maintain a few packages on the [AUR](https://aur.archlinux.org/packages/?K=Schnouki&SeB=m).
- Before that, I had submitted a few Gentoo packages (ebuilds).
- Once upon a time I contributed to the ArchLinux and [FSFE][] mailing lists, and translated a few newsletters for the FSFE.
  But I don't have enough time to do that anymore.
- In 2003-2004, I contributed quite a bit to the **[French Wikipédia][wiki:Schnouki]**: wrote a few articles, translated
  a few ones as well, and wrote a macro to convert OpenOffice.org documents to the Wikimedia syntax :smile: (I even
  wrote a Python script for the XChat IRC client that fixed bad encoding in messages from the "Recent Changes" bot on
  the `#frrc.wikipedia` channel…)



[@Cimbali]: https://github.com/Cimbali
[Caddy web server]: https://caddyserver.com/
[Caddyfile-mode]: https://github.com/Schnouki/caddyfile-mode
[FSFE]: https://fsfe.org/
[GitHub page]: https://github.com/Schnouki
[Hugo]: https://gohugo.io/
[ImageMagick]: https://github.com/ImageMagick/ImageMagick
[MPD]: https://www.musicpd.org/
[PushOver]: https://pushover.net/
[Pympress]: https://github.com/Cimbali/pympress
[QBasic]: https://en.wikipedia.org/wiki/QBasic
[Supélec]: http://www.centralesupelec.fr/
[Turbo Pascal]: https://en.wikipedia.org/wiki/Turbo_Pascal
[ZSH completion for git-annex]: https://github.com/Schnouki/git-annex-zsh-completion
[baguetteBox.js]: https://github.com/feimosi/baguetteBox.js
[collectd]: http://collectd.org/
[devd]: https://github.com/cortesi/devd
[django-modeltranslation]: https://github.com/deschler/django-modeltranslation
[django-weasyprint]: https://github.com/fdemmer/django-weasyprint
[git-annex-remote-hubic]: https://github.com/Schnouki/git-annex-remote-hubic
[git-annex]: https://git-annex.branchable.com/
[glib]: https://developer.gnome.org/glib/
[healthchecks.io]: https://healthchecks.io
[hubiC]: https://hubic.com/
[hugo-baguetteBox]: https://github.com/Schnouki/hugo-baguetteBox
[islas]: https://code.schnouki.net/schnouki/islas
[sorl-thumbnail]: https://github.com/jazzband/sorl-thumbnail
[spop]: https://github.com/Schnouki/spop
[youtube-dl]: https://rg3.github.io/youtube-dl/
[wiki:Schnouki]: https://fr.wikipedia.org/wiki/Utilisateur:Schnouki

[post:android]: {{< relref "/post/2014/2014-08-13 Flashing a stock Android image without wiping user data.md" >}}
[post:openvpn]: {{< relref "/post/2014/2014-12-12 OpenVPN for a single application.md" >}}
