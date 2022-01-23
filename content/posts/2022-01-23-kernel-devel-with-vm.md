+++ 
draft = true
date = 2022-01-23T14:59:54+01:00
publishDate = 2022-01-31
title = "Kernel Development with Virtual Machines"
description = ""
slug = "" 
tags = []
categories = []
externalLink = ""
series = []
+++

With this post I will show you how to configure the environment and have a complete dev and testing for the linux kernel using Qemu and virtual machines.

Most of the similar posts show you the basic stuff, like writing a char device driver and that's it, but in that case you can even just build the module out-of-tree (will see what that's mean) and you don't really need much. At the same time that example is quite useless if you need to do real developmetn.

The limit of this approach is that you need to pass the hardware to test to the vm. This is straighforward for USB, less for PCIe, and for other hardware (like network devices) I don't even know how to do it, but I believe that it's even easier (using some kind of bridge config, or so, maybe it's a content for a next post).

I kept this infos in my notes for some time, now I prefer to share it.
