---
title: "hubiC remote for git-annex"
slug: "hubic-remote-for-git-annex"
date: "2014-06-07 00:31:45"
categories:
  - Software
tags:
  - python
  - git-annex
  - hubic
---

I [still][zsh-completion] love [git-annex][]. And one of the things I like is that it can use many storage backends and
track the location of any data on all of these backends. And in the latest versions, it's quite easy to add support for
new backends. Which I did for [hubiC][], an inexpensive[^1] cloud storage service by OVH.

hubiC provides a nice [API][], which is actually the "usual" OpenStack [SWIFT][] API with a custom authentication system
based on [OAuth 2][]. Using that, I wrote an [external special remote][] that connects git-annex to hubiC. I've been
using it for a few months and I'm quite happy with it. It has the following features:

- written in Python 3
- uses [rauth][] for OAuth 2 authentication and [python-swiftclient][] for the SWIFT storage
- support for common git-annex operations: store, retrieve, check, delete
- connection pooling to improve performances
- everything is encrypted if git-annex is told to do so :smiley:
- the MD5 of each transfered file is checked both on the client and on the server to prevent data corruption
- data can be stored in any SWIFT container to avoid polluting the hubiC web app
- **NEW:** large files are stored in several chunks (of configurable size; defaults to 1 GB) to bypass the hubiC limit of
  5 GB/file and to be more tolerant to network errors or authentication timeouts

The latest release is version 0.3. [Get it while it's hot!][git-annex-remote-hubic]

[API]: https://api.hubic.com/
[OAuth 2]: http://oauth.net/2/
[SWIFT]: http://docs.openstack.org/developer/swift/
[external special remote]: http://git-annex.branchable.com/design/external_special_remote_protocol/
[git-annex-remote-hubic]: https://github.com/Schnouki/git-annex-remote-hubic
[git-annex]: http://git-annex.branchable.com
[hubiC]: https://hubic.com/
[python-swiftclient]: https://github.com/openstack/python-swiftclient
[rauth]: https://rauth.readthedocs.org/en/latest/
[zsh-completion]: /posts/2014/05/28/zsh-completion-for-git-annex/

[^1]: I currently pay 10 €/month for 10 TB of storage (but I only use a little over 1 TB). Before that, I used to
    pay almost 30 $/month for 400 GB of Google Cloud Storage.
