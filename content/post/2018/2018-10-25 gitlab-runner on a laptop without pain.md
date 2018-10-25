---
date: "2018-10-25T09:39:20+02:00"
title: "gitlab-runner on a laptop without pain"
categories:
  - Software
tags:
  - ci
  - gitlab
  - systemd
---

I have several (private) projects hosted on [gitlab.com][] that use [Gitlab CI][gitlab-ci]. Since these are private
projects, I prefer to run their CI pipelines on *private* runners. So I set up [gitlab-runner][] on my Kimsufi server.
It works great! Except that…

Except that my Kimsufi server is **really** slow. So tests that run in 2 to 3 minutes on my laptop sometimes take 20 to
30 minutes to run in CI. Which is not acceptable. I'm therefore running a *second* instance of gitlab-runner, on my
laptop this time. It's much faster! But…

But my laptop is not always on, nor always online. And I don't want CI pipelines to fail because I closed my laptop, put
it in my backpack, and ran to catch my bus home.

So I found a quick and dirty solution: use systemd to start gitlab-runner every morning and stop it every evening
*before* I run catch my bus. So in addition to the standard `gitlab-runner.service` unit, I now have 4 extra systemd
units:

- `start-gitlab-runner.service` and `start-gitlab-runner.timer`, that start gitlab-runner every morning (but only on
  weekdays)
- `stop-gitlab-runner.service` and `stop-gitlab-runner.timer`, that stop it every evening (also only on weekdays).

All of these are available in a [Gist][]:

{{< gist Schnouki a4864a8b7d2299ad477b599e66b24568 >}}

All of these files are installed in `/etc/systemd/system`. Once they're there, a simple `sudo systemctl daemon-reload &&
sudo systemctl enable {start,stop}-gitlab-runner.timer` and it's done.

I've used this for 18 months now and it worked pretty well for me. I don't need to worry about gitlab-runner anymore:
problem solved! :+1:

[gist]: https://gist.github.com/Schnouki/a4864a8b7d2299ad477b599e66b24568
[gitlab.com]: https://gitlab.com/
[gitlab-ci]: https://docs.gitlab.com/ee/ci/README.html
[gitlab-runner]: https://docs.gitlab.com/runner/
