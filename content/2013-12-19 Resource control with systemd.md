Title: Resource control with systemd
Date: 2013-12-19
Category: Software
Tags: systemd, cgroups, linux

My dev environment requires [CouchDB][], [ElasticSearch][], [Redis][], a [Django][] dev server, and a web browser.
Usually I even need two browsers: [Firefox][] and [Chromium][]. And, of course, I run [Emacs][] and a few instances or
[urxvt][].

This takes a lot of resources. And I obviously don't want my laptop to lag because it's swapping or because any service
is hogging the CPU.

Since the biggest offender are ElasticSearch and CouchDB, it's really tempting to use systemd to limit how much memory
they can use. And it turns out that it's extremely easy to do so:

    :::bash
    # cat > /etc/systemd/system/elasticsearch.service <<EOF
    .include /usr/lib/systemd/system/elasticsearch.service

    [Service]
    CPUShares=512
    MemoryLimit=1G
    EOF
    # systemctl daemon-reload
    # systemctl restart elasticsearch

Done! And it's easy enough to do the same with CouchDB or any other memory-eating service. But if I give each of these
services 1G of memory, they can still collectively use too much memory. And if I give them less, some of them will
quickly run out of memory. But it turns out that this is really easy to solve using systemd again: you just have to put
all the services in the same CGroup, and limit the resources for the whole CGroup.

Using recent versions of systemd, this is done using slices. (With older versions you could deal with CGroups directly;
this is not possible anymore, or is at least strongly discouraged, as newer versions use a new, different CGroups
hierarchy.) The principle is almost the same: we create a new slice, assign services to this slice, and limit the
resources for this slice. Again this can be done in a few seconds:

    :::bash
    # cat > /etc/systemd/system/limits.slice <<EOF
    [Unit]
    Description=Limited resources Slice
    DefaultDependencies=no
    Before=slices.target

    [Slice]
    CPUShares=512
    MemoryLimit=2G
    EOF
    # for SERVICE in couchdb elasticsearch redis; do cat > /etc/systemd/system/$SERVICE.service <<EOF
    .include /usr/lib/systemd/system/$SERVICE.service

    [Service]
    Slice=limits.slice
    EOF
    done
    # systemctl daemon-reload
    # systemctl restart couchdb elasticsearch redis

And you can then check that it works using `systemctl status`:

    :::bash
    # systemctl status elasticsearch.service
    elasticsearch.service - ElasticSearch
       Loaded: loaded (/etc/systemd/system/elasticsearch.service; disabled)
       Active: active (running) since Wed 2013-12-18 11:08:07 CET; 35min ago
     Main PID: 28784 (java)
       CGroup: /limits.slice/elasticsearch.service
               └─28784 /bin/java -Xms256m -Xmx1g -Xss256k -Djava.awt.headless=true ...

More docs are available with `man systemd.resource-control` and `man systemd.slice`. Since slices are quite new, there
are not many examples of their use yet, but I'm sure their usage will increase in the future.

[Chromium]: http://www.chromium.org/
[CouchDB]: http://couchdb.apache.org/
[Django]: http://www.djangoproject.com/
[ElasticSearch]: http://elasticsearch.org/
[Emacs]: https://www.gnu.org/software/emacs
[Firefox]: http://mozilla.org/firefox
[Redis]: http://redis.io/
[urxvt]: http://software.schmorp.de/pkg/rxvt-unicode
