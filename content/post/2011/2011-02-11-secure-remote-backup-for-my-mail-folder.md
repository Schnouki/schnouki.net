---
title: "Secure remote backup for my mail folder"
slug: "secure-remote-backup-for-my-mail-folder"
date: "2011-02-11"
categories:
 - Software
tags:
  - backup
  - gnupg
  - encryption
  - rsync
  - mail
---

It is said that *there are two kinds of people in the world: those that have
lost a hard drive, and those that are going to lose a hard drive*. Several weeks
ago, I lost a *huge* hard drive and a *lot* of data. I was able to retrieve
most, but not all of them.


## Remote backups?

Now I regularly do complete incremental backups of my computers on external hard
drives. But in case of *big* trouble (fire, theft...), this is just useless. The
solution is to do additional backups on a remote server.

Last week, I decided to use [rsync.net][] for that. I must say I am very pleased
by this service: it's not that cheap (but affordable, especially when you are
entitled to the [student/teacher/Open Source developer discount][discount]), but
it seems to be very solid, and the support is very competent and quick to answer
any question. So now I am backing up 10+ GB of pictures using [unison][][^1],
and the next step is to store more sensitive data: all my e-mails.

Here is what I want for my e-mails:

- store them all. Currently there are about 7 years of e-mails from 3 different
  accounts, fetched on my laptop using [offlineimap][].
- store them safely. I consider this to be sensitive data, so I want them to be
  encrypted with [GnuPG][].
- sync them efficiently. I don't want to have to upload 1.5 GB just to store 5
  more MB of mail, I want something that works a bit like [rsync][].

I considered different approaches:

- rsync + [sshfs][] + [EncFS][] or [eCryptFS][]: too complicated, probably too
  slow.
- [rsyncrypto][]: too complex (I don't want to have an extra certificate just
  for that), does not seem to be maintained, has annoying dependencies (needs to
  patch gzip).
- [duplicity][]: nice, but I don't need incremental backups.

So in the end I just wrote my own script to do just what I want **=]**


## Introducing `seb`: Simple Encrypted Backup

### How does it work?
`seb` is a simple [Python 3][] script that performs backups quite efficiently.
It produces a bunch of *packs*, which are encrypted tarballs, which can then be
uploaded to the remote host.

A pack contains a fixed number of files (250 in my case, which is reasonable
given that most of my mails are only a few kilobytes). When running `seb`, it
finds which files were added, modified or deleted since its last run. Packs are
then updated to reflect these local changes. `seb` tries to be a little smart
here: instead of creating new packs, it will first try to add new files to packs
that have less than 250 files.

All the needed internal data are saved in a single file, a dictionary that is
serialized using Python's [pickle][] module. File modifications are detected
using their modification times only; this can be an issue, but computing file
hashes seems overkill here: mails are not supposed to change once they are sent
and received...

### Performance
`seb` is quite quick. The longest part of the backup is by far uploading data to
the remote server.

Some statistics:

|                    | Local mail      | Remote backup |
|:------------------ | ---------------:| -------------:|
| Number of files    |          87,107 |           349 |
| Minimum size       |           218 B |      54.89 kB |
| Maximum size       |        16.06 MB |      47.82 MB |
| Average size       |        13.75 kB |       1.65 MB |
| **Total size**     |  **1169.32 MB** | **575.70 MB** |

### How to use?
1. Download `seb`: <https://gist.github.com/821667>
2. Read the doc: `./seb --help`
3. Use: `./seb ~/mail /path/to/backup_fs`

Here's a tip: on the first run, use a local directory as the destination, and
then upload its content to your remote backup site (using scp or rsync for
example). On the subsequent runs (where there will be much less data to
transfer), you can mount your remote backup site using [sshfs][] and use this
mount point directly as your destination folder. It works fine for me.

### How to restore a backup?
1. Grab all the packs.
2. Decrypt each pack with `gpg` and extract it with `tar`.
3. That's all.


[^1]: At the moment, the servers of rsync.net are running unison 2.27.157. Arch
    Linux has 2.32.52 (which is the current stable release), and 2.40.\* is due
    in a few days (next stable release). Problem: 2.2\* is not compatible with
    2.3\*, 2.3\* is not compatible with 2.4\*, etc. So I updated the
    [unison-old][] package on the AUR, which works really fine for me.

    According to the rsync.net support, they will be upgrading Unison on their
    servers this month.

[rsync.net]: http://www.rsync.net/
[discount]: http://www.rsync.net/resources/faq.html#14
[unison]: http://www.cis.upenn.edu/~bcpierce/unison/
[offlineimap]: http://offlineimap.org/
[gnupg]: http://www.gnupg.org/
[rsync]: http://samba.anu.edu.au/rsync/
[sshfs]: http://fuse.sourceforge.net/sshfs.html
[encfs]: http://www.arg0.net/encfs
[ecryptfs]: https://launchpad.net/ecryptfs
[rsyncrypto]: http://rsyncrypto.lingnu.com/
[duplicity]: http://duplicity.nongnu.org/
[python 3]: http://www.python.org/
[pickle]: http://docs.python.org/py3k/library/pickle.html
[unison-old]: http://aur.archlinux.org/packages.php?ID=33399
