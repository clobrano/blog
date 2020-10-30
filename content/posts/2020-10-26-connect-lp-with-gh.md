---
title: "How to use GitHub Actions to connect with Launchpad"
date: 2020-10-26T11:51:15+01:00
draft: true
---

Since the beginning of the Yaru project, three years ago, we always had a little problem: two different places for bug tracing.

Our main repository is hosted on [GitHub](https://github.com/ubuntu/yaru), but we also have the [Launchpad](https://launchpad.net/ubuntu/+source/yaru-theme) page taking care of the `yaru-theme` package.

I can not stress enough how much I appreciate people that use Yaru and take time to report a problem (even when they report it in a not-so-nice way 😀), but somehow we tend to forget LP, and even if the Ubuntu Desktop team took care of them as well, some bugs had to wait too much for a response from our side.

A couple of week ago we decided to handle this with our CI.


Ideally, our solution would have the following:

1. Daily checks.
2. A list of all active bugs Launchpad.
3. For any new bug found, create a GitHub bug with ID, Title and link to the original report.

We already have some GitHub Actions to keep track of our upstreams. It's configured to run periodically and automatically create a PR when there is new content we shall import. This configuration looked promising for the first point.

To interact with Launchpad we have [Launchpadlib](https://help.launchpad.net/API/launchpadlib).

> launchpadlib is an open-source Python library that lets you treat the HTTP resources published by Launchpad's web service as Python objects responding to a standard set of commands. With launchpadlib you can integrate your applications into Launchpad without knowing a lot about HTTP client programming.

Playing with this library is pretty fun, and the best way to learn it is through the [listed examples](https://help.launchpad.net/API/Uses). For instance, I must thank [Bughugger](), that showed me the way to get the list of bugs of a given application.

```py
import os
from launchpadlib.launchpad import Launchpad

HOME = os.path.expanduser("~")
CACHEDIR = os.path.join(HOME, ".launchpadlib", "cache")

lp = Launchpad.login_anonymously(
    "Yaru LP bug checker", "production", CACHEDIR, version="devel"
)

ubuntu = lp.distributions["ubuntu"]
archive = ubuntu.main_archive
packages = archive.getPublishedSources(source_name="yaru")
package = ubuntu.getSourcePackage(name=packages[0].source_package_name)

bug_tasks = package.searchTasks()
for task in bug_tasks:
    print(task)
```

I then extracted three data from the task:
- ID: `task.id`
- Title: `task.title`
- Link: `"https://bugs.launchpad.net/ubuntu/+source/yaru-theme/+bug/" + str(task.id)`

The third point is actually made of two different steps:
1. identify new issues
2. create an issue

Both points have been resolved using [HUB](https://github.com/github/hub).

> hub is a command line tool that wraps git in order to extend it with extra features and commands that make working with GitHub easier.

GitHub provides its own [CLI tool](https://cli.github.com/), which I use on a daily bases, but the point that convinced me to use HUB is the following:

> hub can also be used to make shell scripts that directly interact with the GitHub API.

## Create issues

Let's start from the last step.

Creating an issue with HUB is simple

```sh
hub issue create -m <title> -m <message> -l Launchpad
```

Here I used the `-m` flag twice to set the title:

> LP#[ID] [TITLE]

and the body of the issue:

> Reported first on Launchpad at https://bugs.launchpad.net/ubuntu/+source/yaru-theme/+bug/[ID]

then I added a **Launchpad** label (`-l`), which makes bug management easier, and ended up very useful for the next step.

## Create only NEW bugs

HUB can list all the bugs from the repository, but - at the time of writing - Yaru has more than 1.000 bugs (only 44 open 😀), then it takes a while to get them all for parsing. Luckily, HUB can filter by label!

```sh
hub issue --state all --label Launchpad
```

Parsing the output is easy with Python, all the rest is just a little glue logic to put all together.


# end: the result

I am satisfied with the end result. We can be more responsive to our user base requests, and I had fun writing the [python script](https://github.com/ubuntu/yaru/blob/master/.github/lpbugtracker.py), and learned something new of GitHub Action.
