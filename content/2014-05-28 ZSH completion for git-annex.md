Title: ZSH completion for git-annex
Date: 2014-05-28 0:21
Category: Software
Tags: zsh, git-annex

I love [git-annex][]. It works extremely well, its documentation is excellent, and Joey Hess, its main developper, is
amazingly reactive when you tell him about a bug or ask him any question about this software. I'm currently using
git-annex to manage almost 1 TB of data, spread over my laptop, my NAS, a few external hard drives, and my [hubiC][]
account. (Yes, git-annex is also designed to be able to use many different storage backends, and it's really easy to
write new ones, [which I did got hubiC][git-annex-remote-hubic]; more on that later…)

The biggest ~~issue~~ annoyance with git-annex is the lack of completion when using ZSH. The completion for git is
amazing, so it's quite weird to have nothing for git-annex.

But as often with free software, someone has already started scratching that itch: I found a basic
[completion function for git-annex][completion-function]!
<!-- PELICAN_END_SUMMARY -->
It's for an old version of git-annex, but I've been able to update it to the latest version of git-annex:

- added support for new git-annex subcommands (metadata, groups and wanted content, etc.)
- added better description for common arguments
- added specific arguments to all subcommands
- fixed a bug when attempting to run git-annex in a non-git directory
- update the Python code to Python 3
- fix remotes and backends completion

The updated code is available on <https://github.com/Schnouki/git-annex-zsh-completion>. To install that, just copy the
`_git-annex` file to some directory in your `$fpath` (I use `$HOME/.config/zsh/completion`), and run `autoload -U
path/to/_git-annex`. You will also need to have Python 3 somewhere in your `$PATH` as `python3` (tested with 3.4, should
work with 3.2+).

Many, many thanks to the awesome people who started this completion function: Frank Terbeck and Valentin Haenel. And to
Joey for his amazing work on git-annex.

[completion-function]: https://github.com/esc/git-annex-zsh-completion
[git-annex]: http://git-annex.branchable.com
[hubiC]: https://hubic.com/
[git-annex-remote-hubic]: https://github.com/Schnouki/git-annex-remote-hubic
