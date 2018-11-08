---
date: "2018-11-08T16:51:02+01:00"
title: "Highlighting Hugo shortcodes in Emacs"
categories:
  - Software
tags:
  - emacs
  - Hugo
---

I'm working on some new content for this blog that uses a lot of [shortcodes][]. The problem is that in Emacs,
[markdown-mode][] doesn't know about shortcodes, so it doesn't render them properly:

![Shortcode - not highlighted - bad!](shortcode-bad.png)

Fortunately, a few lines of Emacs Lisp and it works beautifully:

{{< code "markdown-shortcode.el" elisp >}}

![Shortcode - highlighted - good!](shortcode-good.png)

Sure, it's not much. But I like it!

(This requires your Hugo site to be a [Projectile][] project, but since just having it in a git repository is enough,
that should not be a problem…)


[markdown-mode]: https://github.com/jrblevin/markdown-mode/
[Projectile]: https://github.com/bbatsov/projectile/
[shortcodes]: https://gohugo.io/content-management/shortcodes/
