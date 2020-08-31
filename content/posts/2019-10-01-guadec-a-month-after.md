---
date: "2019-10-01T00:00:00Z"
excerpt: I went to GUADEC, what now?
draft: false
share: true
tags:
- gnome
- theme
- yaru
- ubuntu
- guadec
title: Notes about GUADEC 2019
---


This post is incredibly late. After the initial draft (30th of August 😒) many things happened and consumed all my free time, e.g. the last weeks of the Yaru release for Ubuntu 19.10 😊.

 Last August, together with Frederik, I participated to the [GUADEC 2019](https://2019.guadec.org/) conference in Thessaloníki, on behalf of the Yaru team, thanks to the [Ubuntu Community sponsorship](https://clobrano.github.io/blog/i-am-going-to-guadec/). Here is my experience.


## Conferences and talks

The first three days are all about conferences and talks. Since I had planned no talks, I could relax and finally meet many people I have only chatted with online as well as some new ones. This is one of the best things of GUADEC: to finally give a face to online friends and enjoy face to face conversation.

> This is one of the best things of GUADEC: to finally give a face to online friends and enjoy face to face conversation.

It was awesome to spend time with the (partially complete) Ubuntu Desktop team: Marco, Iain, Robert, Ken, Seb, James, as well as Carlos Soriano, who helped me in some Nautilus topics, Carl and Ian from System76 and Cassidy from elementary OS, who also wrote a [great post about his experience here Greece](https://blog.elementary.io/elementary-at-guadec-2019/).

Very pleased also by the community events organized during these first three days.

## BoFs

The second part of GUADEC is dedicated to workshops, also known as **Birds of Feather** or simply [BoF](https://schedule.guadec.org/bofs).

> The term is derived from the proverb "Birds of a feather flock together". The (idiomatic) phrase "birds of a feather" meaning "people having similar characters, backgrounds, interests, or beliefs".
[source: [Wikipedia](https://en.wikipedia.org/wiki/Birds_of_a_feather_(computing))]

 I took part in two of them.

### FreeDesktop Dark Style Preference

The [FreeDesktop Dark Style Preference](https://schedule.guadec.org/bofs/194) BoF[^2] took place, quite shortly indeed, the 26th morning at the beginning of [GTK BoF](https://schedule.guadec.org/bofs/197), since the two workshops shared the same participants. We[^1] discussed the main reasons to have a cross platform Dark Style definition and the main problems (e.g. naming convention, themes that do not provide a dark variant, or themes that provide more than one). It was an introductory discussion, I think there will be more in the future.

### Vendor Themes

The 27th was the time for the [Vendor Themes](https://schedule.guadec.org/bofs/314) BoF, the one I was waiting for. 

There is no doubt that *theming* GTK application is a sensible topic. Some developers do not appreciate/want it[^3], but Neil McGovern, Executive Director of the GNOME Foundation, who organized and moderated the workshop, stated clearly that it is something that GNOME wants to support, and in fact the discussion, with some ups and downs, went really well! 🎉

We agreed to start with a subset of features, differentiating between three main areas:

- **supported**: semantic (e.g. accent colors) and non-semantic colors (palette) and colored headerbars,
- **better do it upstream**: stylistic changes not against upstream positions,
- **here be dragons**: frankly quite clear already.


I liked how **the discussion grew from skeptical to interested**, with the BoF extended a couple of hours more because we were all focused in pushing this forward and convinced that better theme APIs are useful for third party themes as well as for apps developers (branding is not a Distro-only thing after all)[^4].

For more details, Cassidy's post I linked above is a great read, as well as [Tobias' one](https://blogs.gnome.org/tbernard/2019/09/05/guadec-2019/).

## Follow up

An initial organization and work regarding Vendor Themes, renamed *Vendor Styles*, has started immediately:

- A [dedicated topic](https://discourse.gnome.org/t/gtk-adwaita-and-vendor-styles/1641) in GNOME discourse, for discussion and coordination on goals and first steps.
- Initiative for [reviewing the use of custom colors in gtk apps](https://gitlab.gnome.org/GNOME/Initiatives/issues/11).
- [Improved documentation](https://gitlab.gnome.org/GNOME/gtk/commits/wip/jimmac/document-public-colors) 

All the rest is in our hands.

### Conclusion

**GUADEC was a terrific experience for me**. Everything was way out of my usual days, both professionally and personally. If I had to think about getting out of my "comfort zone", I could not have a better way than this and I hope to join again next year, above all if I succeed in be involved in more upstream work.


[^1]: I like *pluralis majestatis*, but I did very little 😊
[^2]: Introduced by Cassidy's [The Need for a FreeDesktop Dark Style Preference](https://www.youtube.com/watch?v=gi_3b81eBUE).
[^3]: With valid points indeed.
[^4]: do you wanna use *green* for some reason? Here is the *Theme's green selection of colors* that goes well with all the other colors.
