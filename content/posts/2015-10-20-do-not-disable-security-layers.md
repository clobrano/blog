---
date: "2015-10-20T00:00:00Z"
excerpt: Bad habits in tutorials, guides, etc.
draft: false
share: true
tags:
- thoughts
- security
title: Do not disable security layers
---

*Disclaimer (sort of): here I am talking from a Software developer point of view AND about open source projects, which is true in most of the cases where I saw the behavior I am about to describe.*

I read a blog post yesterday that is only the last example of a bad practice I saw often: **disabling authentication/security in applications** only because it is annoying to type the password "every time". My point of view in those cases is **do not do it**. Not just because there is a reason to have such security layer - which is true BTW -, but because there are at least two better solutions (and I will give you three):

**It might be a bug**. In that case, the right thing to do would be to open a ticket in the bugtrace and the brilliant thing to do would be to fix that bug.

**The application already provides an automatic authentication method**. [OpenPGP](http://www.openpgp.org/) keys (GPG, PGP, and the likes), encrypted password files and a lot of other things (really fashinating some [proximity sensor based mechanisms](http://www.wired.com/wiredinsider/2014/11/unlock-your-passwords-with-your-proximity/) for example) might be available and the worst thing here is that I am not learning how to use those important technologies if I just "hack" the software security.

If the application does not provide anything like above. This is similar to point 1, I have a **great opportunity to contribute to the project** in a really valuable way!

Hacking, when legal, is good to learn new things, but sometimes it is not the right solution.


