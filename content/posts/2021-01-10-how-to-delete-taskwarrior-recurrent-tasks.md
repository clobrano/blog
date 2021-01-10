---
title: "How to Delete Taskwarrior Recurrent Tasks"
date: 2021-01-10T15:21:06+01:00
draft: true
tags:
- GTD
- Taskwarrior
---


I'm trying out [Taskwarrior](https://taskwarrior.org/) as CLI task manager, because [it can be paired](https://github.com/clobrano/script-fu/commit/75961580cfddd38048ca74e1bedad44e13942454) with my [Letsdo](https://github.com/clobrano/letsdo) for time tracking and it's very flexible, but today I got stuck with a bunch of "recurring tasks".

Taskwarrior lets you set a task "recurring", that is, it shows up at some time intervals and you are supposed to set it to "DONE" every time, which is good to take into account things I do on a monthly base, but it turned out the be faulty for daily activities at work. During this Christmas holidays, in fact, the daily recurring tasks accumulated in a tragic manner, so I decided to get rid of them altogether, but how?

Taskwarrior has the following CLI format

```sh
$ task [filter] [command]
```

then I first tried the simplest command

```sh
$ task recur delete
```

which was suppose to delete all recurring tasks. However this acts also on the hundreds of already completed task, and being Taskwarrior (dutily) pedantic, after 5 minutes confirming that "yes indeed I know this task is recurring and I do want to delete it", I stopped and summoned The Internet. [Which worked pretty well](https://stackoverflow.com/a/59119791/1197008)

So, thanks to "dustymabe" on StackOverflow, I know that I shall delete only the "original" recurring task.

```sh
$ task all +PARENT
ID St UUID     Age Done Project Tags R Due        Description
60 R  6524a8cd 5w       hsw          R 2020-11-30 timetracker
36 R  6cff76be 11w      hsw          R 2020-10-14 daily task review
35 R  ad77b550 12w      hsw          R 2020-10-12 code-review

$ task 35 36 60 delete
```
