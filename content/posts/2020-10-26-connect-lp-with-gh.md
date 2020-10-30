---
title: "How to use GitHub Actions to connect with Launchpad"
date: 2020-10-26T11:51:15+01:00
draft: true
---

# intro: the problem

[Yaru]() is a Community project lead by a small group of maintainers.

Yaru is a Community project maintained on GitHub, which a package repository on Launchpad.

In the three years since it's start, the Yaru project (born as Communitheme) has always kept its bugs in GitHub.

In the last month in Yaru team we discussed how to solve the problem of multiple bug sources.

In Yaru we had the problem of having 2 different places to look for bugs

Since the beginning of the Yaru project three years ago we always had a little problem: two different places for bug tracing.

Our main repository is hosted on [GitHub](), but we also have the [Launchpad]() page taking care of the yaru-theme.* package.

I can not stress enough how much I appreciate people that use Yaru and take time to report a problem (even when they report it in a not-so-nice way 😀), but somehow we tend to forgot LP, and some bugs had to wait too much time for a response from the Yaru team. The Ubuntu Desktop team took care of them in our behalf, so many thanks to them as well, but a couple of week ago we decided to handle this with our CI.



two places to look for bugs

ideally, packaging issues in lp, the other in github, but what's the right separation and is the user responsible for chooseing?

always be thankful for reports, is our responsibility to look for bugs.

moreover, they are just 2 places (except forums)


# core: the solution

github has a CI system which we can use

launchpad has a cool python library binding to query data

it lacks of documentation, but luckily there are (old) project using it, for example: https://launchpad.net/bughugger

getting all the bugs.

how to connect with our repo

let gh action create the bugs for us.

# end: the result

we have automatically created issues in gh. We can look for it immediately and respond. The LP bug numbers are decreased?

further improvement: anynymous, we can't operate on LP.
