---
title: "HOWTO Backup your GnuPG secret key on paper"
slug: "howto-backup-your-gnupg-secret-key-on-paper"
date: "2010-03-22"
categories:
  - Software
tags:
  - howto
  - backup
  - gnupg
---

Paper is a safe way to backup a secret key: you can't hack into it remotely, you
can hide it very easily, and you will still be able to use it in 50+ years. No
USB stick can do that...

If you want to store your GnuPG secret key on a paper sheet, it is quite simple
to do. You can use [PaperKey][], a small tool that strips all the useless data
from a secret key and formats it into a printable result. This is great, but the
result can be quite long: printing my 2048 bits secret key would take 3 pages.

But there is a nice way to store more data on a small surface: 2D barcodes, for
example in the [DataMatrix][] format, using the great [`libdmtx`][libdmtx] library. For
small keys, this is really easy:


~~~console
gpg --export-secret-key KEY_ID | paperkey --output-type raw | dmtxwrite -e 8 -f PDF > secret-key.pdf
~~~

If your key is bigger (like my 2048 bits key), you will need to split it in
several parts, because the result of the `paperkey` command will be too big to
be encoded in a single DataMatrix. Here is a simple method:

~~~bash
# Generates key-aa, key-ab, ...
gpg --export-secret-key KEY_ID | paperkey --output-type raw | split -b 1500 - key-

# Convert each of them to a PNG image
for K in key-*; do
    dmtxwrite -e 8 $K > $K.png
done
~~~

You now have several PNG images that you can print together on a single page.

----

To restore your key, it's just as simple: scan each DataMatrix into a separate
image, decode them with `dmtxread`, concatenate all the resulting files
(`cat`...), and use `paperkey`:

~~~console
cat my-scanned-keys | paperkey --pubring ~/.gnupg/pubring.gpg > secret-key.gpg
~~~

----

Source: [TPK Archival](http://www.mail-archive.com/gnupg-users@gnupg.org/msg10827.html) (by
David Shaw, creator of [PaperKey][]).


[paperkey]: http://www.jabberwocky.com/software/paperkey/
[datamatrix]: http://en.wikipedia.org/wiki/Data_matrix_%28computer%29
[libdmtx]: http://www.libdmtx.org/
