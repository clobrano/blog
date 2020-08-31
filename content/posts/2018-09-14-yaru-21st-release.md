---
date: "2018-09-14T00:00:00Z"
excerpt: Yaru 21st stable release
draft: false
share: true
tags:
- yaru
- ubuntu
- gnome
- communitheme
- theme
- opensource
title: Yaru 21st stable release
---

The **Yaru team** is happy to announce a new stable release!

![yaru-release-pic](/images/ubuntu-yaru.png)

This was the week of [Cosmic Cuttelfish UI Freeze](https://wiki.ubuntu.com/CosmicCuttlefish/ReleaseSchedule), this means that, from now on we won't see any new UI styling, but only bug fixing and improvement "under the hood".

Since last release we had tons of contributions, here a short list:

- Improvement in our build script. Improvement is a bit reductive... Among the other awesome things, our build system is now ready to deploy an independent Yaru-dark theme (that is yet to come, though)
- Restyle of the *default button*
- New Suru Icons
- Refinements of Nautilus selected icons
- Improved dark variant style of switches, check-and-radio buttons
- Use normal icons in message tray
- Review selected page in emoji picker
- Dropped custom fix for Chrome/Chromium windows controls, that now work fine all alone \0/
- Make scrollbars background transparent, adapting to other scrollbars
- Restyled notebook tabs in dark variant to look more similar to Gnome-Terminal ones
- infobar enhancement
- releasing package yaru-theme version 18.10.3


Yaru is already default theme in Cosmic Cuttlefish 18.10!

If you want to try it on [Ubuntu 18.04](https://www.ubuntu.com/download/desktop), install the [snap](https://snapcraft.io/communitheme) package from GNOME Software or from SHELL using the following command

{{< highlight bash >}}
snap install communitheme
{{< / highlight >}}

This will install the **stable** Snap package, which will be automatically updated ~each week, but if you want to try immediately any new change, install from the *edge* channel.

{{< highlight bash >}}
snap install communitheme --edge
{{< / highlight >}}


A [Yaru inspired Firefox theme](https://color.firefox.com/?theme=XQAAAALtAAAAAAAAAABBKYhm849SCiazH1KEGccwS-xNVAWBveAusLC2VAlvlSjJ6UJSeqAgCYbdwa_-rV70IROd68eEot6ey6DBD6clRBXp1e7Wbm3jkhhZsTB6iGtxUNA9rD_f7WkYu4v4RFB_XR74DFyPAFWYVQkUMNbL2Mo2sQa9jDMc35kqQOoJm4_aT6Dkc9xrEV6O_-5hkDwOlMzIcFLFRtRxRaGEyH-y4Be72Vgc9j_f_vkOgA) is available, but, please consider that *this is not part of Communitheme official release*.
