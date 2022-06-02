+++ 
draft = true
date = 2022-05-19T19:18:12+02:00
title = "Kernel Development with QEMU Virtual Machines (part 2)"
description = ""
slug = ""
authors = []
tags = ["Linux", "kernel", "Virtualization", "QEMU" ]
categories = []
externalLink = ""
series = []
+++

This is an update of [my previous post](/posts/2022-04-30-kernel-devel-with-vm/) about using virtualization to work with the Linux Kernel, which brings with two new points:

1. A different way to mount the QEMU image using a QEMU tool in place of guestmount.
2. USB pass-through, which is fundamental when working with USB drivers.


## QEMU-nbd to mount the QEMU image

In the [previous post](/posts/2022-04-30-kernel-devel-with-vm) I suggested to use _guestmount_ to mount the VM (QEMU) image into the guest filesystem in order to install the kernel modules, however I had some issues on Ubuntu lately[^1] and could not use it. Looking for alternatives I found that QEMU project already has a tool for such purpose called [qemu-nbd](https://qemu.readthedocs.io/en/latest/tools/qemu-nbd.html). A big plus is that you likely have it already installed, since it comes with _qemu-utils_ package, and from a rapid view it does much more that just mounting the image [^2].

Qemu-nbd _exports a QEMU disk image as [Network Block Device](https://en.wikipedia.org/wiki/Network_block_device) (from which NBD[^3])_, fulfilling my simple goal with the following two passages 

1. Load the kernel module and connect the NBD device to the image
    ```bash
    $ sudo modprobe nbd max_part=3
    $ sudo qemu-nbd --connect=/dev/nbd0 /path/to/image
    ```

    `max_part` is the option that specifies the maximum number of partitions we want `nbd` to manage. Since the machine I installed in the previous post had the filesystem on sda3, `max_part=3` is enough.

2. At this point each partition in our image will be exposed via a `/dev/nbd0pX` device, which we can mount.
    ```
    bash
    $ sudo mount /dev/nbd0p3 /mnt/tmp
    ```

Once the kernel modules are installed into the image, we can unmount it

```bash
$ sudo umount /mnt
$ sudo qemu-nbd --disconnect /dev/nbd0
```

Cool!


## USB pass-through

There is a fast way and a better way to allow USB pass-through

**The easy way** is to use the `-device` switch (see [this](https://qemu.readthedocs.io/en/latest/system/devices/usb.html)) to add an USB controller to the Virtual machine in a way that as soon as the USB device is connected to the hardware the Guest OS will pass it through, making it available for testing your kernel drivers.

There are countless of flags and filters, for example you could pass the entire bus, but I prefer to be specific and pass the precise device via it's Vendor and Product ID, adding the following line to the QEMU argument list

```bash
-usb -device usb-host,vendorid=0x1bc7,productid=1066
```

but you also need to run QEMU with superuser privilegies, so something like this
```bash
sudo qemu-system-x86_64 \
    -pidfile /tmp/qemu.pid \
    -enable-kvm \
    -drive file=$DISK \
    -m $RAM \
    -kernel $KERNEL \
    -append "root=/dev/sda3 console=ttyS0 rw" \
    -serial mon:stdio \
    -display none \
    -usb -device usb-host,vendorid=0x1bc7,productid=1066   
```

**A better way** is to us [Spice](https://www.spice-space.org)

> Spice is an open remote computing solution, providing client access to remote displays and devices (e.g. keyboard, mouse, audio). The main use case is to get remote access to virtual machines, although other use cases are possible and in various development stage.

Install the dependencies first

```bash
sudo apt install spice-gtk spice-vdagent
```

To make it work we need to use the QXL/SPICE display method (`-vda qxl`) and to enable the spice server in qemu-kvm (`-spice port=5900,addr=127.0.0.1,disable-ticketing=on`).

Finally we shall instruct qemu to emulate the USB via the XHCI controller (`-device qemu-xhci,id=spicepass`) and configure some channel for USB redirection. The following will create 1 channel

```
-chardev spicevmc,id=usbredirchardev1,name=usbredir \
    -device usb-redir,chardev=usbredirchardev1,id=usbredirdev1
```

Packing it all together it looks like this


...

as a bonus we can enable clipboard sharing between host and guest adding the following line

```bash
-device virtio-serial-pci \
-device virtserialport,chardev=spicechannel0,name=com.redhat.spice.0 \
-chardev spicevmc,id=spicechannel0,name=vdagent
```



[^1]: The previous post was written using OpenSuse Tumbleweed as test machine
[^2]: I need to look into it asap.
[^3]: Countless the times I wrote the acronym in the wrong order (ndb, bnd, bdn, ...).
