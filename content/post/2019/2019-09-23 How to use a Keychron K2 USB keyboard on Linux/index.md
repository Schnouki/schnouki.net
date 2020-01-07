---
date: "2019-09-23T23:41:00+02:00"
lastmod: "2020-01-07T15:35:34+02:00"
title: How to use a Keychron K2/K4 USB keyboard on Linux
slug: how-to-use-a-keychron-k2-usb-keyboard-on-linux
categories:
  - Software
tags:
  - linux
  - keyboard
cover: KeychronK2.jpg
---

I recently bought a Keychron K2 mechanical keyboard and it's been great so far. Most things work out of the box on my
Linux laptop with a few notable exceptions:

- function keys!
- no insert key!

---

The issue with function keys:

- when set to Windows mode, the special keys ("volume up", "brightness control", etc.) send Windows-specific key
  combinations instead of standard keycodes that Xorg recognizes.
- when in Mac mode, the Fn key seems useless, there's no way to enable function keys (to have F12
  instead of "volume up"), and the "Command" and "Option" key don't match the usual order of the Super and Alt keys.

The solution is simple:

- use the keyboard in Mac mode (so that it sends useful keycodes instead of Windows-specific shortcuts)
- configure the Linux `hid_apple` driver to use function keys and swap "Option" and "Command" by creating
  `/etc/modprobe.d/hid_apple.conf` with the following content:

    ```
    # For Keychron keyboard -- https://wiki.archlinux.org/index.php/Apple_Keyboard
    options hid_apple fnmode=2 swap_opt_cmd=1
    ```

You'll need to reboot (or unplug the keyboard, unload the module, reload it with the correct options, and plug the
keyboard), and *voilà*, it works :)

---

Now, for the lack of Insert key. I mostly use it in the Shift+Insert combination to paste things from the X primary
selection.

The simplest solution I found is to use `xmodmap` to map Shift+Delete (which I never use) to Shift+Insert. To do that, I
created `~/.Xmodmap` with the following content:

```
keycode 119 = Delete Insert Delete Insert
```

And added this to my `~/.xinitrc`:

```sh
# Load .Xmodmap if it exists
[[ -f ~/.Xmodmap ]] && xmodmap ~/.Xmodmap
```

---

There's also a list of resources for Keychron K2 Linux users in [this Git
repo](https://github.com/Kurgol/keychron/blob/master/k2.md), and on Facebook Keychron created a [Keychron Linux User
Group](https://www.facebook.com/groups/Keychronlinux/).

---

**EDIT:** everything in this post also applies to the Keychron K4 keyboard.
