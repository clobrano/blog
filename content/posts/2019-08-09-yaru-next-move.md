---
date: "2019-08-09T00:00:00Z"
excerpt: new course of Yaru development
draft: false
share: true
tags:
- yaru
- ubuntu
- theme
- adwaita
- guadec
title: Yaru next move
---

Yaru news!

In the last months the work on Yaru master branch looked slower than usual, but under the hood some important things were changing.

Starting from the release of the **new Adwaita theme** with GTK 3.32 and the discussion about **custom GNOME themes**, we acknowledged that

- some application developers had serious problems developing for too many variants
- we did not want to waste the great work upstream is doing refreshing GNOME look and feel, providing new features and fixing other problems.

so we tried to find a middle ground where both parts can feel satisfied.

The Yaru team (but mostly Frederik, who did a great job) took a new, more upstream oriented, contribution approach, proposing some of its solutions and ideas to GNOME developers, that - as always stated - have been quite open to consider, discuss and in some cases accept 🎉.

This was fundamental to reduce the customization needed for Yaru and other theme variations and allowed us to work internally developing and testing a **huge rebase on the newest Adwaita**.

The result of this work landed in master branch at the beginning of this week. It has not been released officially yet, but we hope it will be soon, and in the meantime **we would be glad if anyone wants to test it and give us constructive feedback**.

We solved the "customization theme problem"? Well, surely not. We alone, as Yaru team, cannot of course.

We kept the distinctive Yaru traits and reduced some big differences from Adwaita, so that (hopefully) GNOME application developers won't find as many surprises as they had in the past, and we think that this is important. [We will also take part in the next GUADEC](https://clobrano.github.io/blog/i-am-going-to-guadec/), where [Vendor Themes](https://wiki.gnome.org/GUADEC/2019/Hackingdays/VendorThemes) will be discussed again and we will try to give our best in future developments.

Stay tuned!

NOTE: This same post is published first on the [Ubuntu discourse](https://discourse.ubuntu.com/) HUB at this [link](https://discourse.ubuntu.com/t/yaru-next-move/12155)
