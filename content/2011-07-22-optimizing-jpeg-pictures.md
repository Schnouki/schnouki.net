Title: Optimizing JPEG pictures
Date: 2011-07-22
Category: Software
Tags: jpeg, shotwell, howto

I recently realized that during our vacation in London, my girlfriend and me
took about 4 GB of pictures. Since I currently have 30 GB of storage space on
[rsync.net][] to do my backups, 4 GB is quite a lot. Fortunately, there are
several solutions to reduce their size.

The first one would be to resize them or to increase their compression ratio /
decrease their quality. But I don't want such a lossy method: I want to keep my
pictures at the best quality available so I can print them in high resolution if
I want to.

The other solution is to "optimize" them. Once again, several methods: removal
of unnecessary data (EXIF markers and other metadata), conversion to
[progressive JPEG][progressive], or [Huffman table optimization][huffman]. Since
I don't want to lose metadata (mostly because I add many tags to my pictures in
[Shotwell][] and they are stored in these metadata), I only use the other two
methods.

Most of my photos are taken with my camera (Panasonic Lumix FZ100) or with my
girlfriend's (Nikon Coolpix S8000).

I first tried to use [jpegoptim][] to do this task. It only optimizes Huffman
tables, and it does it well. However, this tool only supports EXIF and IPTC
metadata, and on pictures taken with my camera, Shotwell stores its tags in the
XMP "Subject" marker. And jpegoptim erases XMP markers when processing them,
resulting in many lost tags...

So I tried to use [jpegtran][] to do the same. It also supports progressive
JPEG, and is apparently much better at not destroying metadata when not asked to
do so :) Here is the command I use to optimize my pictures with it:

    :::sh
    parallel -u 'echo {}; jpegtran -optimize -progressive -perfect -copy all -outfile {}.tran {} && mv {}.tran {}' ::: *.JPG

`parallel` is [GNU Parallel][parallel], a tool which is very useful to speed
things up by using the 16 cores of my work PC to do the job :)

Using `jpegtran` this way, I reduced the size of my "London" folder from 4.0 GB
to 3.5 GB, i.e. a 12.5% reduction with absolutely no quality loss. Not bad!

Now, some funny things I noticed while doing this:

-   the Lumix FZ100 does not do any optimization to its JPEG files: `jpegtran`
    always reduced them by at least 13%, sometimes more. It also create some
    EXIF and XMP markers in its files, but no IPTC tag.

-   the Coolpix S8000 does a *much* better job at optimizing its files: `jpegtran`
    could only reduce their size by 0.6 to 0.8%, 1.2% at best. It creates EXIF,
    XMP *and* IPTC markers.

-   when Shotwell stores tags directly into pictures, it will use the IPTC
    "Keywords" marker *only if there already are IPTC data in the file*. This is
    why `jpegoptim` lost tags on pictures taken with my camera: the FZ100 only
    added XMP markers, which were then wiped out by `jpegoptim`. For pictures
    taken with the S8000, tags were stored both in XMP and IPTC markers, so when
    the XMP ones were removed, Shotwell still took the IPTC version into
    account.

    Not sure if it's a bug or a feature...


[rsync.net]: http://rsync.net/
[progressive]: http://www.faqs.org/faqs/jpeg-faq/part1/section-11.html
[huffman]: http://www.impulseadventure.com/photo/optimized-jpeg.html
[shotwell]: http://yorba.org/shotwell/
[jpegoptim]: http://freshmeat.net/projects/jpegoptim/
[jpegtran]: http://jpegclub.org/
[parallel]: http://www.gnu.org/s/parallel/
