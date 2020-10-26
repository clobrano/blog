---
title: "How to use GitHub Actions to connect with Launchpad"
date: 2020-10-26T11:51:15+01:00
draft: true
---

# intro: the problem
yaru is a community project hosted on GitHub, but our ubuntu package is hosted in Launchpad

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
