---
date: "2017-07-05T00:00:00Z"
excerpt: ""
draft: false
share: true
tags:
- opensource
title: My First Contribution to GNOME Calendar
---

I am not totally new to open source contributions. Luckily enough, I have both some spare time to contribute to the communities I like and a Company that wants me to support some open source projects (see [UbuntuCore](https://www.ubuntu.com/core) and [ModemManager](https://www.freedesktop.org/wiki/Software/ModemManager/)). However, I have never written anything about that. I'd like to, but usually my patches provide improvements that a "normal user" can hardly see (like udev rules management, or better support for [3G/4G modems](http://paldan.altervista.org/telit-plugin-improvements-modemmanager/)), so that it is hard to explain the delta provided.

This time though, my contribution to GNOME Calendar is more visible, so I'd like to show it :)

**I'm an Ubuntu user since Feisty Fawn (2007), and a GNOME user since**. I think I've tried every DE flavour (KDE, Elementary's Pantheon, LXDE, even Enlightenment 17), but I've always returned to GNOME. Then, during the transition from GNOME2 to GNOME3, **I learnt to love Unity** instead<a rel="nofollow" href="#footnote1" id="ref_footnote1"><sup>1</sup></a>. Finally, [the end of Unity](https://insights.ubuntu.com/2017/04/05/growing-ubuntu-for-cloud-and-iot-rather-than-phone-and-convergence/) makes me look at GNOME again and since I wanted to give back something to the communities of both Ubuntu and GNOME, I started looking at the [Newcomers Guide](https://wiki.gnome.org/Newcomers).


> The Newcomers Guide is for developers who want to participate in coding GNOME's apps

Two projects were (and are) interesting to me, [Polari](Polari) and [Calendar](Calendar), but I am not very familiar with javascript, yet, and I have always preferred using my calendars from a desktop application than from the "famous-web-based-one", so I chose the latter.

The first newcomers Calendar bug I saw was this one<a rel="nofollow" href="#footnote2" id="ref_footnote2"><sup>2</sup></a>:

> [Show weekday instead of date in the create event popover when creating new event within a week](https://bugzilla.gnome.org/show_bug.cgi?id=747479)


I took this one for the following reasons:

1. I though "Ok, it's for newcomers, it shouldn't be that hard" and I was kind of wrong :D
2. I had enough search keywords to look into the code and find the right spot to work in. I was right, here :)

The real challenge wasn't really the feature itself, but the fact that the displayed text should be easily translated. Ideally, developers should reduce repetition as much as possible (DRY principle, right?), but translators need context to do their job.

Let's make a simple example. To generate a messages like this one:


> "New event from next Monday to next Tuesday"

I would have provided a template like "New event from next %s to next %s" and using some calendar function to automatically replace the strings with the right weekday name. I learned instead that in some languages (Polish, I'm talking to you!) the translation of the word "next" might have different form for different days of the week. So, in general, I should keep some context around the constant strings I wanted to use.

I was amazed by this little intricacies, but at the same time I've never worked with translation before (gettext was only a dependency I always forgot to install before building some projects), so I really appreciated the support given by maintainers and translators, both on the bug and on IRC, that encouraged me to progress into the development.

So, cutting a long story short, after 8 patch versions :D, this is the outcome. It is a matter of taste, but I hope you like it, because [it is in master now](https://git.gnome.org/browse/gnome-calendar/commit/?id=9033d98) :D

<figure>
    <img src="/images/2017-07-05/new-event-today-old.jpg" width="400" height="290">
   <figcaption>New Event Today, old version</figcaption>
</figure>

<figure>
    <img src="/images/2017-07-05/new-event-today-new.jpg" width="400" height="290">
    <figcaption>New Event Today, new version</figcaption>
</figure>

<figure>
    <img src="/images/2017-07-05/multiday-old.jpg" width="400" height="290">
    <figcaption>New Multiday Event in the current week, old version</figcaption>
</figure>

<figure>
    <img src="/images/2017-07-05/multiday-new.jpg" width="400" height="290">
    <figcaption>New Multiday Event in the current week, new version</figcaption>
</figure>

<figure>
    <img src="/images/2017-07-05/future-event-old.jpg" width="400" height="290">
    <figcaption>New Event in 7 days from Today, new version</figcaption>
</figure>

<figure>
    <img src="/images/2017-07-05/future-event-new.jpg" width="400" height="290">
    <figcaption>New Event in 7 days from Today, new version</figcaption>
</figure>

#### Footnotes
1. Not love at first sight, but it became the first and last DE I didn't need to heavily hack soon after fresh install. It was just right ;(<a rel="nofollow" href="#ref_footnote1" id="footnote1">[↩]</a>.
2. Well not really, first there was a little fix in it's json file, but it is not really much<a rel="nofollow" href="#ref_footnote2" id="footnote2">[↩]</a>.
