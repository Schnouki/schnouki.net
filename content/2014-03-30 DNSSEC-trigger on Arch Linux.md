Title: DNSSEC-trigger on Arch Linux without Network Manager
Date: 2014-03-30
Category: Software
Tags: dns, dnssec, unbound, linux

Many ISPs have pretty shitty DNS resolvers. Sometimes they act as fake DNS, sometimes they are just poorly configured.
And it's even worse on hotspots with captive portals.

Part of the solution is to use [DNSSEC][]… but it's not that easy. Of course, [Unbound][] can be installed in a matter
of minutes, but it's not necessary a good idea to always use a full resolver instead of the ISP caching resolvers, and
it can break on hotel networks as it can't resolve the (bad) hostname of the captive portal.

A nice solution is to use [DNSSEC-trigger][]:

> Dnssec-trigger reconfigures the local unbound DNS server. This unbound DNS server performs DNSSEC validation, but
> dnssec-trigger will signal it to use the DHCP obtained forwarders if possible, and fallback to doing its own AUTH
> queries if that fails, and if that fails prompt the user via dnssec-trigger-applet the option to go with insecure DNS
> only.

<!-- PELICAN_END_SUMMARY -->

DNSSEC-trigger can also detect hotspots with captive portals, open the login page, and wait until login before
configuring Unbound correctly. An excellent introduction to this awesome tool is available in French on
[Stéphane Bortzmeyer's blog][bortzmeyer] and in English on [Jan-Piet Mens's blog][jpmens].

Installing it on Arch Linux is quite easy as it's already packaged on the AUR:

    :::console
    $ yaourt -S dnssec-trigger

However this only works with Network Manager or netconfig. Which sucks as I only use plain-old [dhcpcd][] and
[wpa_supplicant][]. Luckily, it's actually quite easy to get it working with dhcpcd: you only need a script started by
dhcpcd that will tell the dnssec-trigger daemon about the IP addresses of the new DNS servers, and to disable a call to
a Network Manager-specific script when the dnssec-trigger daemon is started. Long story short, just copy this to
`/usr/lib/dhcpcd/dhcpcd-hooks/19-dnssec-trigger`:

    :::bash
    # Notify dnssec-trigger about the new DNS IPs

    run_dnssec_trigger()
    {
        syslog info "dnssec-trigger(dhcpcd) detected $interface DNS $new_domain_name_servers"
        dnssec-trigger-control submit "$new_domain_name_servers"
    }

    # For ease of use, map DHCP6 names onto our DHCP4 names
    case "$reason" in
    BOUND6|RENEW6|REBIND6|REBOOT6|INFORM6)
        new_domain_name_servers="$new_dhcp6_name_servers"
        ;;
    esac

    if $if_up || [ "$reason" = ROUTERADVERT ]; then
        run_dnssec_trigger
    fi

And delete the `ExecStartPost=` line from `/usr/lib/systemd/system/dnssec-triggerd.service` (the best way is to copy it
to `/etc/systemd/system/dnssec-triggerd.service`). Now reload systemd and start dnssec-triger:

    :::console
    # systemctl daemon-reload
    # systemctl start dnssec-triggerd

I've been running this for almost 2 months, and it works flawlessly.

[DNSSEC-trigger]: https://www.nlnetlabs.nl/projects/dnssec-trigger/
[DNSSEC]: https://en.wikipedia.org/wiki/Domain_Name_System_Security_Extensions
[Unbound]: https://unbound.net/
[bortzmeyer]: http://www.bortzmeyer.org/dnssec-trigger.html
[dhcpcd]: http://roy.marples.name/projects/dhcpcd/index
[jpmens]: http://jpmens.net/2011/10/21/automating-unbound-for-dnssec-on-your-workstation/
[wpa_supplicant]: http://hostap.epitest.fi/wpa_supplicant/
