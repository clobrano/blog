---
date: "2019-02-05T00:00:00Z"
excerpt: Yaru 28th stable release
draft: false
share: true
tags:
- yaru
- ubuntu
- gnome
- communitheme
- theme
- opensource
title: Yaru 28th stable release
---

The **Yaru team** is happy to announce the second stable release of 2019.

![yaru-release-pic](/images/ubuntu-yaru.png)

Here the main content:

- Improved render-bitmaps helper scripts
- Released on Disco Dingo 19.04
- Actually release Yaru-dark in debian package (sorry)
- Updated and improved symbolic icons 
- Added new icons for Polari, Firefox and Quadrapassel (okay, those could change in the future, considering the big-discussion-in-the-sky about Icons)
- Adding new application-x-trash mimetype which is consistent with clock on image-loading icon
- Bring back symbolic icons for the app menu and the notitications/message
- Update readme with up-to-date screenshots
- Add icon for missing image
- OGA file extension for sounds
- Update Contributing with needed steps before building
- Adapt gtk tooltips border to shell
- Add a build option to install compatibility stubs for communitheme theme name.
- Update "sound" part in contributing guideline
- Many bug fixing and optimizations e.g. in Infobars, pathbar and switches


If you want to try it on [Ubuntu 18.04](https://www.ubuntu.com/download/desktop), install the [snap](https://snapcraft.io/communitheme) package from GNOME Software or from SHELL using the following command

{{< highlight bash >}}
snap install communitheme
{{< / highlight >}}

This will install the **stable** Snap package, which will be automatically updated at each stable release, but if you want to try immediately any new change, install from the *edge* channel.

{{< highlight bash >}}
snap install communitheme --edge
{{< / highlight >}}
