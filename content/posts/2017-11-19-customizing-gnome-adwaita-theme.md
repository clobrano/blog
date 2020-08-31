---
date: "2017-11-19T00:00:00Z"
excerpt: how to test changes to the official GTK+ theme
draft: false
share: true
tags:
- opensource, gnome
title: Customizing Gnome Adwaita theme
---

This is a quick note about testing changes to the official GNOME GTK+ theme [Adwaita](https://blog.gtk.org/2016/06/22/adwaita/)<a rel="nofollow" href="#footnote1" id="ref_footnote1"><sup>1</sup></a>.

During this Summer, I contributed to other CSS-based themes, but Adwaita is different for two main reasons:

1. it uses [Sass](http://sass-lang.com/).
2. it is released in binary form as a **gresource**.

I used *Sass* for fun some time ago, hopefully I will remember it quickly, but as a **gresource**, the theme is loaded into memory and there are no *.css* files to modify on the fly. So I spent some time this weekend to understand how to test the changes on the theme.  

The solution I have tried works fine, but it looks sub-optimal to me. I am pretty sure that should be possible to do something with [jhbuild](https://developer.gnome.org/jhbuild/stable/introduction.html.en), but since I did not find a way so far, here is how I am going to play with Adwaita theme:

* copy Adwaita folder from `/usr/share/themes` into the hidden `.themes` folder in Home (after a fresh install, it does not exist, so I created it).

{{< highlight bash >}}
mkdir -p ~/.themes
cp -r /usr/share/themes/Adwaita/ ~/.themes
{{< / highlight >}}

* change its name to make it easier to distinguish between the original and the copy when selecting the theme.

{{< highlight bash >}}
cd  ~/.themes
mv Adwaita AdwaitaMod
cd AdwaitaMod
sed -i "s/Adwaita/AdwaitaMod/g" index.theme
{{< / highlight >}}

* get a copy of *gtk+* project<a rel="nofollow" href="#footnote1" id="ref_footnote2"><sup>2</sup></a>.

{{< highlight bash >}}
cd ~/workspace
git clone git://git.gnome.org/gtk+
{{< / highlight >}}

* copy gtk+'s Adwaita folder content into a *gtk-3.0* inside the folder made at step 2.

{{< highlight bash >}}
cd ~/.themes/AdwaitaMod/gtk-3.0
cp -r ~/workspace/gtk+/gtk/theme/Adwaita/* .
{{< / highlight >}}

* change *gtk.css* `@import` directive to import the local *gtk-contained.css* file (or its dark version).

{{< highlight bash >}}
$ cat gtk.css
@import url("gtk-contained.css");
{{< / highlight >}}

* finally, install *sassc* to compile *.scss* files into *.css*

{{< highlight bash >}}
sudo apt install sassc
{{< / highlight >}}

To make any change to the .scss files visible, run the `parse-sass.sh` script to update *gtk-contained.css* file.


# Notes
1. A couple of days ago I volunteerd for the Ubuntu [theme refresh](https://community.ubuntu.com/t/call-for-participation-an-ubuntu-default-theme-lead-by-the-community/1545) project, that aims to renew Ubuntu theme starting from Adwaita<a rel="nofollow" href="#ref_footnote1" id="footnote1">[↩]</a>.
2. I actually got mine using jhbuild, but that would be too long and not necessary so far<a rel="nofollow" href="#ref_footnote2" id="footnote2">[↩]</a>.
