---
date: "2018-09-06T17:17:40+02:00"
title: "Backup TOTP secrets with Emacs"
categories:
  - Software
tags:
  - emacs
  - security
  - OTP
  - org-mode
  - gnupg
---

I use [FreeOTP](https://freeotp.github.io/) to generate time-based OTP tokens on my phone. It's similar to Google
Authenticator *et al*, except that it's Free Software, it works really well, and it can display images in addition to an
account name, which is *nice*.

![Screenshot](https://freeotp.github.io/img/android.png)

Plus it's really easy to use: start setting-up the 2nd factor authentication on the service you want, when it shows a
QR-code scan it with the app, and you're done. Yeah, just like *every* other TOTP app.


But as I'm a little paranoid, I want to have a full backup of all my OTP secrets somewhere safe… So I did just that
using Emacs, org-mode, and some Python.

The idea is to use an org-mode file with a big table with several columns:
- Issuer: the name of the service: Google, Amazon AWS, OVH, Sentry…
- Label: the account identifier: username, email address, account number, etc.
- Secret: the base32-encoded shared secret. The most important field: this is what is actually used to generate the
  one-time passwords.
- Image: optional, the name of an image file (hosted on my server) to be displayed in FreeOTP.
- URI: the content of the configuration QR-code. This column is generated by org-mode using a column formula and the
  content of the other columns :+1:

To fill this table, I created 2 backup scripts, one for Google Authenticator (used to migrate away from it :wink:), and
one for FreeOTP. And then I wrote *another* script that uses [qrencode](https://fukuchi.org/works/qrencode/) to generate
QR-codes as ASCII art and store them in the very same Org file… So I can very easily re-add accounts to the app or to
another device.

How to use:

1. Add a new service using FreeOTP
2. In the Org file, run the FreeOTP backup script (put the cursor on it and press `C-c C-c`): the result appears under the script
3. Copy the secret in a new line in the table
4. Fill the rest of the line (issuer, label, image if wanted, and put the image on my server if needed)
5. Generate the URI by updating the table (put the cursor on it and press `C-c C-c`)
6. Regenerate the QR code by running the appropriate script (put the cursor and *guess what you need to do now*)
7. Re-add the service to FreeOTP with the new QR-code that includes a nice image :wink:

Here is the code:

{{< code "files/2018/OTP-backup.org" org >}}

For additional fun, I save this file in a secure location and encrypt it with GnuPG. Again, it's really easy in Emacs:
just save the file as `OTP-backup.org.gpg`, and it will ask for the details before passing the file to GnuPG.

I've been using this file for several years now and I'm really, *really* happy with it.

**Warning:** your Android phone needs to be rooted and to have USB debugging enabled for the backup scripts to work.