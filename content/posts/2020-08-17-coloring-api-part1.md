---
date: "2020-08-17T00:00:00Z"
excerpt: Gnome is working on a real Themes support
draft: false
share: true
tags:
- gnome
- theme
- Slimbook
title: My part in A Coloring API for Gnome
---


I should start writing about this, regardless of how this effort will end up with, and make it public, in the hope that this will:

- push me through it, considering the little amount of time I can dedicate
- help me remember where I was, after some possible intervals of doing other things
- bring some more skilled people around to try and help me 😀

The starting point is the excellent [Adrien Plazas' post](https://aplazas.pages.gitlab.gnome.org/blog/blog/2020/04/02/coloring-api.html) about the outcome of GNOME's [Design Tools Hackfest 2020](https://wiki.gnome.org/Hackfests/DesignTools2020), which in turn follows up the GUADEC 2019 [vendor themes BoF](https://wiki.gnome.org/GUADEC/2019/Hackingdays/VendorThemes) which I took part in.

My goal in this is to help developing some API to allow a certain level of Gnome personalization for application developers first, and distributions then. To do this, Gtk/Shell CSS stylesheets shall use the CSS exported color variables like `@theme_bg_color`, `@theme_selected_bg_color`, etc., which means all the SASS files shall use them too, and this finally leads to stop using some SASS features (e.g. `if/else` and color functions like `lighten`, `darken`, ecc.) which work with constant color values only.


## Disclaimer

There's some clear external resistance in doing this, but for what I could understand not for the feature itself, which is what I'd like to provide.

As part of the Yaru team, I understood that the bugs we're facing lately will be very hard to fix the old way, also considering the rapid development of some new cool gtk features[^libhandy], and whatever some people might think, nobody likes to ship apps with visual defects. However, I think it is right for App developers, as well as for Distributions, to show their brand somehow.

While it is possible to break an app with bad theme support - and by broken I mean unusable in some way - I am not aware of any broken app at the moment of writing. If you know better, please consider opening a fix request at the [Yaru project](https://github.com/ubuntu/yaru/issues). However since "broken" doesn't only mean unusable, please consider it even if Yaru just behaves weird on any app you use.

Finally, consider that being the dark headerbar the main source of such possible problems, **Yaru has a light version**, with a light headerbar, and your app should look better with that.


## What I did so far

I installed a fresh Fedora 32 on [the kindly sponsored Slimbook](https://twitter.com/carlolobrano/status/1266808827405578242). I can not thank enough the people at [Slimbook](https://slimbook.es/en/), because I can now dedicate a full machine only for this purpose, instead of using my daily driver (which I can't risk to break too much).

Then I contacted Gnome devs on IRC at **#gnome-design** to get some hints and, thanks to them, I started immediately playing with Gtk directly in [Gnome Builder](https://wiki.gnome.org/Apps/Builder), instead that configuring jhbuild, which was what I expected to be forced to 😓.

So, the plan was:

1. develop a simple test app as part of **gtk-demo**, which is run automatically form Gnome Builder
2. tackle the two most common patterns identified by Adrian:

   > Common patterns in vendor themes are to change the accent color from the default blue to something better matching their brand like orange or green, another is to have a light theme but a dark titlebar as do Ubuntu and Pop!OS.

About this, I started with the accent colour, thinking it would be easier, but I recognized that the primary problem should be to convert all the sass functions into gtk CSS one

Now, this is the list of gtk color functions available:

> "rgba", "rgb", "lighter", "darker", "shade", "alpha", "mix"

and this the list of sass functions used in Adwaita css

> lighten, darken, mix, desaturate, transparentize, invert

Unfortunately `lighter` and `darker` cannot be used, since they apply a fixed color change (about 30% variation), while the correspondent `lighten` and `darken` take the amount as second paramenter, but I hope to get something working using `shade` instead.

Well, that's enough for now. If not for other, this exercise will improve my blogging skills 😀


[^libhandy]: If you think about **libhandy**, yes I think about this too.
