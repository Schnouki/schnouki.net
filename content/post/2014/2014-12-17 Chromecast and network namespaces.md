---
title: "Chromecast and network namespaces"
slug: "chromecast-and-network-namespaces"
date: "2014-12-17"
categories:
 - Software
tags:
  - howto
  - openvpn
  - privacy
  - security
  - vpn
  - chromecast
  - avahi
  - mdns
images:
  - /img/2014/chromecast/result.png
---

This is a follow-up to the post about [OpenVPN for a single application]({{< relref "2014-12-12 OpenVPN for a single application.md" >}}).

I've finally found a way to access my [Chromecast][] from a [program][popcorntime] running inside a network namespace!
And it turns out it's pretty easy to do.

With the setup I described in my last post, the isolated app has full access to the local network through the `vpn1`
interface. The only thing needed for the Chromecast to work is that the application must be able to *discover* the
Chromecast on the LAN.

<!--more-->

The Chromecast discovery process uses mDNS (aka Bonjour, ZeroConf or whatever), which on Linux is usually handled by
[Avahi][]. Basically, to discover Chromecasts on your LAN, you just have to do discover a device that publishes a
`_googlecast._tcp` PTR record. The human-friendly way to do this is to use `avahi-discover-standalone`. On my laptop, it
gives me the following result:

![All the available mDNS services on my WLAN](/img/2014/chromecast/discover_global.png)

The issue is that inside the network namespace, the mDNS query will be sent on the `vpn1` interface, but it won't be
routed to the WLAN interface, so there won't by any response:

![Only the services from my laptop from the VPN namespace](/img/2014/chromecast/discover_vpnns_no_reflector.png)

The only visible services are the ones from my laptop, and not the other ones from the WLAN.

However, there's a very simple way to resolve this: it's to configure Avahi to proxy all the mDNS queries to all the
available network interfaces! This feature is called "reflector", and is a enabled by a one-line change in
`/etc/avahi/avahi-daemon.conf`:

~~~ini
[reflector]
enable-reflector=yes
~~~

Restart Avahi (`systemctl restart avahi-daemon`; reloading it is not enough here!) and try to run
`avahi-discover-standalone` again:

![All the services -- on the vpn1 interface!](/img/2014/chromecast/discover_vpnns_reflector.png)

Much better! :smiley: The device can now be discovered, and applications running in the network namespace can therefore
use it at will.

![Final result](/img/2014/chromecast/result.png)

Thanks to [Joel Knight][source] for the tip!

[Avahi]: http://avahi.org/
[Chromecast]: https://www.google.com/chrome/devices/chromecast/index.html
[popcorntime]: https://popcorntime.io/
[source]: http://www.packetmischief.ca/2012/09/20/airplay-vlans-and-an-open-source-solution/
