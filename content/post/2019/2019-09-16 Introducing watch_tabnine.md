---
date: "2019-09-16T17:00:00+02:00"
title: Introducing watch_tabnine
categories:
  - Software
tags:
  - D
  - TabNine
  - linux
---

I'm a big fan of [TabNine](https://tabnine.com/), a super nice code editor-agnostic code completion tool. I use it from
Emacs using [`company-tabnine`](https://github.com/TommyX12/company-tabnine) and it's amazing how well it works
(especially since I joined the beta for the new cloud-based service that uses deep learning techniques to provide better
completion candidates).

However there's one annoying thing with TabNine. From time to time it starts eating my memory like crazy, first the RAM
and then the swap. This has been reported to the author but not fixed yet as it's probably very hard to reproduce[^1].
Some days everything goes smoothly, some other days I have to restart it 5 times in an hour. Super annoying.

So I wrote a little tool to handle that for me. It checks how much memory TabNine is using, and kills it if it's too
much. This isn't a problem since Emacs restarts it as needed, and it "solves" this issue for me.

I've named this `watch_tabnine` [^2] and it's available on [Sourcehut](https://git.sr.ht/~schnouki/watch_tabnine).

As I recently started learning the [D programming language](https://dlang.org/), I wrote this in D. It went *okay*, as
the result is probably much lighter than its equivalent in Python or Go, and much safer than C. So I'll consider this a
win 😃

Anyway, if you use TabNine and also have troubles with its memory usage, please consider giving it a try!


[^1]: If I wanted to troll, I'd also mention that TabNine is written in Rust, and that for that language memory-safe
    apparently doesn't mean safe for your laptop memory 😃
[^2]: As you probably know, "there are two hard things in computer science: cache invalidation, naming things, and
    off-by-one errors" ([source](https://twitter.com/codinghorror/status/506010907021828096)). And I consistently suck
    at naming things.
