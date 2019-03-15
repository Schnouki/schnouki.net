---
date: "2019-03-15T14:40:31+01:00"
title: "Automatically archive the modules of the currently running kernel on upgrade on Arch Linux"
categories:
  - Software
tags:
  - linux
  - pacman
  - arch linux
  - howto
---

I don't reboot my laptop very often. My current uptime is 11 days; that's quite low, I'm pretty sure the previous one
was at least a month. Yet I often upgrade my system with `pacman -Syu` (or more precisely [`yay -Syu`][yay]). As a
consequence, I'm often running a kernel that is older that the one that is currently installed:

```zsh
~ % uname -sr
Linux 4.20.13-arch1-1-ARCH
~ % pacman -Qi linux | grep Version
Version                  : 5.0.1.arch1-1
```

This is usually fine, except when I plug a new device (for example a USB stick or a memory card) that is handled by a
kernel module that hasn't been loaded yet. Since the current kernel and its modules are not available anymore, the
device doesn't work… And I don't want to reboot just for that.

I found a simple solution using Pacman hooks. The idea is to create a new hook that runs when the `linux` package (or
any `linux-*` package) is upgraded or removed, and that will archive the corresponding modules as a tarball. This way I
can easily extract the tarball and replug my device to have the running kernel autoload the needed module if needed.

This hook needs 2 files:

- the hook file used by pacman to decide if and when the hook command must be run;
- the actual hook command: a shell script that handles archiving the modules directory.

The hook file installed as `/etc/pacman.d/hooks/keep_kernel_modules.hook`:

{{< code "keep_kernel_modules.hook" ini >}}

And the shell script is installed as `/usr/local/bin/keep_kernel_modules.sh`:

{{< code "keep_kernel_modules.sh" >}}

I've been running this for 3 years now without any issue.


[yay]: https://github.com/Jguer/yay
