---
date: "2019-03-12T00:00:00Z"
excerpt: Yaru 29th stable release
draft: false
share: true
tags:
- yaru
- ubuntu
- gnome
- communitheme
- theme
- opensource
title: Yaru 29th stable release
---

The **Yaru team** is happy to announce the third stable release of 2019.

![yaru-release-pic](/images/yaru-19.04.png)


This release brings a lot of changes, specially in **Yaru** icon set.

The *squircle* approach was awesome, but fragile when facing the fact that not all the icons will have the same shape, so we decided to drop it. However, Suru design was so good that it shines even removing the *squircled* background, so we - and when I say we, I actually mean @feitchmeier, @madsrh, @ubuntujagger and @eaglers :D - put a huge effort in this Yaru icon revival, which looks even better than before.
Of course, **we welcome any project that likes the idea to provide its icon in this shape**, so the next big effort will be to describe the new guidelines openly.

Another big news is that Yaru on 18.04 will diverge from Yaru on newest releases.
Recently upstream changes and the new Gnome shell 3.32, made us decide to keep the current style fixed in Bionic Beaver and keep following upstream in Disco Dingo (and next Ubuntu releases) only. Of course, this refers only to the new things that are not compatible to the old version of Gnome Shell and GTK.



If you want to try it on [Ubuntu 18.04](https://www.ubuntu.com/download/desktop), install the [snap](https://snapcraft.io/communitheme) package from GNOME Software or from SHELL using the following command

{{< highlight bash >}}
snap install communitheme
{{< / highlight >}}

This will install the **stable** Snap package, which will be automatically updated at each stable release, but if you want to try immediately any new change, install from the *edge* channel.

{{< highlight bash >}}
snap install communitheme --edge
{{< / highlight >}}
