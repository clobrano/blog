---
date: "2016-07-12T00:00:00Z"
excerpt: Backward compatibility for applications that need old core libraries
draft: false
share: true
tags:
- microblogging
title: Multiple versions of core libraries
---

This is just a reminder to myself, in case I will need it in the future.

Some days ago I was discussing this interesting problem: _how to manage applications that need different versions of some core libraries (e.g. glibc)?_

As example, if we have an application that needs a shared library with soname `reallyneedthis.so.1`, I can package the application together with that library, but it is not that simple for core libraries.

Then, a few days later, I used `LD_LIBRARY_PATH` to test a custom version of ModemManager<a rel="nofollow" href="#footnote1" id="ref_footnote1"><sup>1</sup></a> and I light switched on in my head. Can we use `LD_LIBRARY_PATH` for core libraries?

Unfortunately it is not that easy, because some absolute paths are hard-coded at link time<a rel="nofollow" href="#footnote2" id="ref_footnote1"><sup>2</sup></a> (e.g. ld-linux.so.2 from glibc) and there might be other problems too.

The easiest solution would require to build the application with the new/old glibc (or with something like [rtldi](http://bitwagon.com/rtldi/rtldi.html)) using the --dynamic-linker flag (ELF executable). However rebuild is not an option, usually, and then things get trickier. One solution would be to "instruct" the linker before running the application

{{< highlight bash >}}
$ /path/to/new/libc/ld-linux.so.2 --library-path /path/to/lib <binary>
{{< / highlight >}}

Some articles I read suggest also the *chroot* solution, but I still need to see this solution better.

---

1. The system was using the wrong library after installation ( see also [could not find symbol X](http://clobrano.github.io/blog/undefined-symbol/))
2. Those static paths are the ones reported by "ldd"<a rel="nofollow" href="#ref_footnote2" id="footnote2">[↩]</a>.
