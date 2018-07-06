---
title: "Last commit in each git branch"
slug: "last-commit-in-each-git-branch"
date: "2015-07-28T14:28:00"
categories:
 - Software
tags:
  - git
  - zsh
---

At work we're usually working on many [git][] branches at the same time, and from time to time we rebase the
"work-in-progress" branches on top of `master`. In the end it makes it quite complicated to know when a remote branch
was last modified, by whom, and whether it has been merged or not. So we have to run `git branch -a` and then `git log`
on each remote branch... Too tedious for me, let's automate this :wink:

{{< gist Schnouki 765d18c9317a08b05fde >}}

Save this file somewhere in your `$PATH` (`~/bin` for me), and run `git branch-last-commit` with the same options as
`git branch`.

It's not much, but I like it :blush:

![Screenshot](/img/2015/git-branch-last-commit.png)

[git]: http://git-scm.com/
