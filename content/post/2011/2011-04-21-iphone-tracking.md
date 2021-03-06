---
title: "iPhone tracking"
slug: "iphone-tracking"
date: "2011-04-21"
categories:
  - Software
tags:
  - iphone
  - gps
  - python3
  - apple
---

There has recently been a
[lot](http://radar.oreilly.com/2011/04/apple-location-tracking.html) of
[noise](http://gizmodo.com/#!5793925/your-iphone-is-secretly-tracking-everywhere-youve-been)
about a tool made by Alasdair Allan and Pete Warden:
[every iPhone is tracking its owner's movements all the time][iphone tracker].
For the record, the existence of this database on each iPhone with iOS 4.x has
been documented for [several months](http://blog.csvance.com/?p=39) already. And
it's not really surprising... Remember [Eben Moglen's talk][eben] at FOSDEM
2011?

Now, time for a confession: I have an iPhone too. It's a nice, mostly useless
device, but it becomes quite fun to use once you jailbreak it. And since I
jailbroke mine, I can have fun with it. Now, let's have fun with this
geolocation database.

## Accessing the geolocation database...
First, ssh into your jailbroken iPhone as root (or mount it with ifuse: `ifuse
--root /path/to/mountpoint`). The DB is stored in the
`/var/root/Library/Caches/locationd` folder and is named `consolidated.db`, just
as explained on the [iPhone Tracker][] page. On my phone, it's a 5.4 MB file.
You can copy it to your computer (using `scp`, `rsync`, or just `cp` if you're
using ifuse).

If you're curious, you can then investigate the content of this file using
`sqlite3` or a GUI such as [sqliteman][]. Here are a few interesting tables:
`celllocation`, `celllocationlocal`, and `wifilocation`.

The first one is the one used by Alasdair Allan and Pete Warden in their "iPhone
Tracker" tool. On my phone, there are 2,624 records in this table (timestamp,
latitude, longitude, altitude, plus some other columns), the oldest one are 2.5
months old (February 5th -- FOSDEM!). It would seem that these records indicate
the [positions of cell towers](http://blog.csvance.com/?p=136) rather than your
own, but
[this can only be guessed](http://www.fsf.org/blogs/community/5-reasons-to-avoid-iphone-3g)
since you can't have a look at the iOS source code...

The second table has a similar structure, but apparently a different content. I
did not investigate further (yet).

The last one is a little different: `wifilocation`. It stores the position of a
lot of MAC addresses (with, of course, an associated timestamp). I don't know if
these are the MAC addresses of some wireless access points or the MAC addresses
of wireless *clients*, but given that on my phone there are *35,770* records
since February 6th, I doubt these are just access points.

## ...for fun and profit
The [iPhone Tracker][] seems to be a very nice program, but it's for Macs only.
So I hacked a little Python script that can read such a database and produce a
[KML][] file that can be then viewed using [Google Earth][].

The script is available here: [iphone-tracker.py][]. No dependencies except for
[Python 3](http://python.org/). Very simple to use:

~~~console
$ ./iphone-tracker.py path/to/consolidated.db > output.kml
~~~

The result can then be opened in Google Earth. The positions are grouped by day
to avoid having 2500+ points overlapping on a map.

It can be seen, as described by the researchers who first found out about this,
that the stored positions are far from being precise. The recorded timestamps
are very approximate too. But the simple fact that so many data are stored about
one's location is *really* concerning.

Several months ago, someone also made a
[web viewer](http://www.courbis.fr/Localisation-iPhone-votre.html) where you can
upload you database file and see the result in Google Maps (in French).

## What now?
As far as I know, Apple has not made a public statement about this little
controversy yet. But I'm really eager to see what they will tell about it -- if
they care to tell something about it.

I'm also deeply concerned about the `wifilocation` table of this database,
which, in some aspects, is much worse than the `celllocation` table (no need for
your phone to store that: your network operator already has the data, and it's
probably far easier for your government to ask them than to get access to your
phone).

If it contains geolocation data of wireless access points, this could cause
problems similar to [what Google encountered in Germany][germany], when Google
Cars were gathering data about wireless networks in addition to the Google
Street View pictures.

But if the `wifilocation` table actually contains the last seen location of
wireless *clients*, it could mean that your phone can be used to prove that you
were close to a specific person (identified by his phone wireless MAC address)
at a specific moment. And, for some persons, in some countries, this is a
*serious* reason to worry.

If you wish to disable this database on your (jailbroken) iPhone, you may use
[this workaround](http://technicalmusings.blogspot.com/2011/04/ios-consolidateddb-workaround-for.html).


[kml]: http://code.google.com/apis/kml/documentation/
[google earth]: http://earth.google.com/
[iphone tracker]: http://petewarden.github.com/iPhoneTracker
[sqliteman]: http://sqliteman.sf.net/
[eben]: http://www.youtube.com/watch?v=qol6f-QbrAE#t=3m20
[iphone-tracker.py]: https://gist.github.com/934357
[germany]: http://www.spiegel.de/netzwelt/web/0,1518,690600,00.html
