Title: OpenVPN for a single application on Linux
Date: 2014-12-12
Category: Software
Tags: howto, openvpn, privacy, security, vpn

It's sometimes useful to run a single application through a VPN for [privacy reasons][popcorntime]. There are many ways
to do it, and the most common one is apparently to run the application with a different user account and use some
iptables magic to configure a specific routing table for this user. In my opinion this is way too troublesome and
complicated, and much less comfortable to use. Luckily there's another way to do that on modern Linux systemd:
[network namespaces][netns].

<!-- PELICAN_END_SUMMARY -->

Here's how to run OpenVPN and a single other application in a separate namespace:

1. Get an account with an OpenVPN provider; [FrootVPN][] is free (at the moment) and works great.
2. Create the net network namespace:

        :::console
        # ip netns add frootvpn

3. Start the loopback interface in the namespace (otherwise many things don't work as expected…)

        :::console
        # ip netns exec frootvpn ip addr add 127.0.0.1/8 dev lo
        # ip netns exec frootvpn ip link set lo up

4. Create virtual network interfaces that will let OpenVPN (in the namespace) access the real network, and configure the
   interface in the namespace (`vpn1`) to use the interface out of the namespace (`vpn0`) as its default gateway

        :::console
        # ip link add vpn0 type veth peer name vpn1
        # ip link set vpn0 up
        # ip link set vpn1 netns frootvpn up
        # ip addr add 10.200.200.1/24 dev vpn0
        # ip netns exec frootvpn ip addr add 10.200.200.2/24 dev vpn1
        # ip netns exec frootvpn ip route add default via 10.200.200.1 dev vpn1

5. Enable IPv4 routing and NAT for the interface in the namespace. As my default interface is a wireless one, I use
   `wl+` (which may match `wlan0`, `wlp3s0`, etc.) in iptables for the outgoing interface; if you use a wired interface
   you should probably use `en+` (or `br+` for a bridged interface)

        :::console
        # iptables -A INPUT \! -i vpn0 -s 10.200.200.0/24 -j DROP
        # iptables -t nat -A POSTROUTING -s 10.200.200.0/24 -o wl+ -j MASQUERADE
        # sysctl -q net.ipv4.ip_forward=1

6. Configure the nameserver to use inside the namespace

        :::console
        # mkdir -p /etc/netns/frootvpn
        # echo 'nameserver 8.8.8.8' > /etc/netns/frootvpn/resolv.conf

7. Almost done, now we should have full network access in the namespace

        :::console
        # ip netns exec frootvpn ping www.google.com

8. Finally start OpenVPN in the namespace

        :::console
        # ip netns exec frootvpn openvpn --config /etc/openvpn/frootvpn.conf

9. Once `tun0` is up in the namespace, you're ready to start the program you wanted!

        :::console
        # while ! ip netns exec frootvpn ip a show dev tun0 up; do sleep .5; done
        # ip netns exec frootvpn sudo -u $MYSELF popcorntime

10. It works!

Since this is a little long to do, I wrote a little helper script to manage the VPN namespace, and another script to run
[any app I want][popcorntime] in this namespace. They are available in [this gist][gist].

The only issue I still have is how to let the application inside the namespace access my Chromecast… If anyone has
ideas, I'm interested :smiley:

[gist]: https://gist.github.com/Schnouki/fd171bcb2d8c556e8fdf
[netns]: https://lwn.net/Articles/580893/
[popcorntime]: https://popcorntime.io/
[FrootVPN]: https://www.frootvpn.com/
