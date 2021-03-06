---
title: "OpenPGP smartcard setup on Arch Linux"
slug: "openpgp-smartcard-setup-on-arch-linux"
date: "2010-05-19"
categories:
  - Software
tags:
  - fsfe
  - gnupg
  - security
  - encryption
  - paranoia
---

After I joined the [FSFE Fellowship][fsfe] a few months ago, I received a nice
OpenPGP smartcard. Now I'm using it for real, and I like it!

I've decided to buy two OpenPGP card readers on [Kernel concepts][]:

- *Gemalto PC Express card* for my laptop
- *SCM SCR-335* for my workstation

Both are very easy to get working on [Arch Linux][]: just install `ccid` and
`pcsclite` from the [AUR][], restart udev, start `pcscd` (`/etc/rc.d/pcscd
start`), plug your reader in, and you're good to go.

The next step is to create a key to be used with the card. There is a good
[tutorial][] on this topic on the FSFE Wiki. Only one step can be greatly
enhanced: step 12, "Removing the master key from the keyring". Here is a *much*
easier version:

1. Backup your public key: `gpg --armor --export 559C215F > publickey.asc`
2. Remove your private *and* public key from your keyring:
`gpg --delete-secret-and-public-key 559C215F`
3. Import your public key: `gpg --import publickey.asc`
4. Edit your key and set its trust level to Ultimate: `gpg --edit-key 559C215F`,
`trust`, `5`, `save`, `quit`
5. Make GPG check your smartcard and recreate the secret key stubs by itself:
`gpg --card-status`

That's it! Now you can return to the tutorial and test your card.

~~~nohighlight
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA1

And don't forget to have fun!
-----BEGIN PGP SIGNATURE-----
Version: GnuPG v1.4.10 (GNU/Linux)

iQEcBAEBAgAGBQJL8+C0AAoJEMPdciX+bh5InokH/17+dG0bYU05dTqHVOIDUKch
dGJ75jnO3cci9UcZeqghyH0Odi1uPpidRLWKjd1EogHNo24fb6/CwyL+6yUgW/RF
No0YOKG2r6dJGqpD91v5afd70JSkwMo66CRBpsou5TM6b6bG2p6dHVg3r2pJOKwJ
WoMbrsgHAAX7pGpAjhjREMLTIADwh5+5d1aQJx3qTjWNh908PVm+KN1iT9eryBWE
UJb98O6Zj02I4OTX3VsBmC29FyjfISBJ7LIElZQFTV7I3BIE+FDK9H9Hnb/3psF+
G/VOgHPILzd+BxuUzo4PGVne2GMPHv6vmm+yQlgvuz5Bnn/duU8gWVc+erDC2xQ=
=K7tA
-----END PGP SIGNATURE-----
~~~

*Many thanks to the people involved in [this thread][gpgml] on the GnuPG mailing
list for the tip!*

[fsfe]: http://fellowship.fsfe.org/
[kernel concepts]: http://www.kernelconcepts.de/en/index.shtml
[arch linux]: http://www.archlinux.org/
[aur]: http://aur.archlinux.org/
[tutorial]: https://wiki.fsfe.org/Card_howtos/Card_with_subkeys_using_backups
[gpgml]: http://lists.gnupg.org/pipermail/gnupg-users/2010-March/038535.html
