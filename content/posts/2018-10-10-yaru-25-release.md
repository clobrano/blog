---
date: "2018-10-10T00:00:00Z"
excerpt: Yaru 25th stable release
draft: false
share: true
tags:
- yaru
- ubuntu
- gnome
- communitheme
- theme
- opensource
title: Yaru 25th stable release
---

The **Yaru team** is happy to announce a new stable release, the one that will
be shipped in the upcoming **Cosmic Cuttlefish 18.10 release**!

![yaru-release-pic](/images/ubuntu-yaru.png)

This week release brings the following

- Gnome-software styling improvements in application list
- dash-to-dock transparency fix[^dock]
- Shell: removed black line in highlighted submenu
- Green buttons now have a nicer white outline (normal buttons will still have
    the orange one)
- Fixed the icon used by System Monitor app

[^dock]: The *dash-to-dock* version shipped with Cosmic handles transparencies in a slightly different way, respect the version in Bionic. The result is that we will have the same transparency between Panel and Dock in Cosmic only, while in Bionic, the dock will be slightly more transparent than the Panel.

If you want to try it on [Ubuntu 18.04](https://www.ubuntu.com/download/desktop), install the [snap](https://snapcraft.io/communitheme) package from GNOME Software or from SHELL using the following command

{{< highlight bash >}}
snap install communitheme
{{< / highlight >}}

This will install the **stable** Snap package, which will be automatically updated ~each week, but if you want to try immediately any new change, install from the *edge* channel.

{{< highlight bash >}}
snap install communitheme --edge
{{< / highlight >}}


A [Yaru inspired Firefox theme](https://color.firefox.com/?theme=XQAAAALtAAAAAAAAAABBKYhm849SCiazH1KEGccwS-xNVAWBveAusLC2VAlvlSjJ6UJSeqAgCYbdwa_-rV70IROd68eEot6ey6DBD6clRBXp1e7Wbm3jkhhZsTB6iGtxUNA9rD_f7WkYu4v4RFB_XR74DFyPAFWYVQkUMNbL2Mo2sQa9jDMc35kqQOoJm4_aT6Dkc9xrEV6O_-5hkDwOlMzIcFLFRtRxRaGEyH-y4Be72Vgc9j_f_vkOgA) is available, but, please consider that *this is not part of Communitheme official release*.
