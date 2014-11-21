Title: Flashing a stock Android image without wiping user data
Date: 2014-08-13 23:58
Modified: 2014-11-21 08:40
Category: Software
Tags: Android

Until today my [Nexus 10][] was running Android 4.4.2 (stock firmware from Google). I couldn't install the OTA update to
4.4.4 because I had installed a custom recovery ([TWRP][]) in order to root the device. So today I decided to reinstall
the stock recovery and install the update... But the installation failed. The tablet was able to reboot, but it showed
that is was still running Android 4.4.2, but cound not find any update anymore. Weird...

(IMHO the problem that happened is that when I reinstalled the stock recovery, I installed the version from the 4.4.4
firmware, but the OTA update expected to have the version from the 4.4.2 firmware. Can this cause the install to fail
like this? Not sure, but I have no other explanation.)

So in order to update to 4.4.4 without wiping my device I had to do it by hand:

- download the [latest factory image][factory]; in my case the file is named `mantaray-ktu84p-factory-74e52998.tgz`
- extract the archive: `tar xvf mantaray-ktu84p-factory-74e52998.tgz`
- extract the image zip inside the extracted folder:

        :::console
        $ cd mantaray-ktu84p
        $ mkdir image
        $ cd image
        $ unzip ../image-mantaray-ktu84p.zip`

- flash the boot, recovery and system images, but **not** the userdata one (as it would wipe my data) [[source]](http://forum.xda-developers.com/showpost.php?p=47474021&postcount=26):

        :::console
        $ adb reboot bootloader
        $ # Wait until the device reboots to the bootloader...
        $ sudo fastboot flash boot boot.img
        sending 'boot' (4784 KB)...
        OKAY [  0.739s]
        writing 'boot'...
        OKAY [  0.132s]
        finished. total time: 0.871s
        $ sudo fastboot flash recovery recovery.img
        sending 'recovery' (5334 KB)...
        OKAY [  0.783s]
        writing 'recovery'...
        OKAY [  0.152s]
        finished. total time: 0.935s
        $ sudo fastboot erase system
        ******** Did you mean to fastboot format this partition?
        erasing 'system'...
        OKAY [  0.048s]
        finished. total time: 0.048s
        $ sudo fastboot flash system system.img
        erasing 'system'...
        OKAY [  0.028s]
        sending 'system' (652994 KB)...
        OKAY [ 95.901s]
        writing 'system'...
        OKAY [ 19.227s]
        finished. total time: 115.156s

- start the system from the bootloader.

And voilà! The device booted to Android 4.4.4 and I didn't lose my data. However root access was lost, but that is
extremely easy to restore:

- download [TWRP][] and [SuperSU][]
- reboot the device to bootloader: `adb reboot bootloader`
- flash the custom recovery: `sudo fastboot flash recovery openrecovery-twrp-2.7.1.0-manta.img`
- boot to recovery and enable sideloading (in Advanced --> ADB Sideload)
- sideload the SuperSU zip: `adb sideload UPDATE-SuperSU-v2.02.zip`
- reboot and start the SuperSU app.

I'm sure all of this is common knowledge for a lot of people. But it's not obvious to me, so I'm just putting it here
for the next time I need it :)

**EDIT:** Just tried it and I can confirm that it works well to upgrade from Android 4.4.4. to Android 5.0 "Lollipop"!

[Nexus 10]: https://www.google.com/nexus/10/
[SuperSU]: http://download.chainfire.eu/supersu
[TWRP]: http://teamw.in/project/twrp2
[factory]: https://developers.google.com/android/nexus/images
