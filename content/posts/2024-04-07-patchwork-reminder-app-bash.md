+++
title = "Patchwork Reminder App in Bash"
date = 2024-04-07T17:35:14+02:00
draft = false
+++

Everybody knows [cron jobs](https://www.redhat.com/sysadmin/linux-cron-command), right? But not everybody knows its sibling `at`.

As you might anticipate, if `cron` is used to schedule tasks that are repeated periodically, Linux must have something else to schedule one-time tasks, and this is `at`.


I "discovered" `at` when I wrote a [Pomodoro timer in bash](https://github.com/clobrano/Redtimer), and I periodically went back to it. One of this times, I got struck by this nice use case described in its readme (*Courtesy of tldr*)

```bash
$ tldr at
 at Executes commands at a specified time. More information: <https://man.archlinux.org/man/at.1>.
 ...
 - echo
     "notify-send 'Wake up!'" | at 11pm Feb 18
```

I know this is equivalent to any calendar notification, but spending most of my time in a Terminal and not wanting to pollute my calendar with silly reminders, I found this idea quite intriguing.

Moreover, `at` supports smart dates like "tomorrow", "5pm next week", "next month" and so on, like the new shiny fancy reminder apps!

**So, what is it missing then?**

1.  I don't want to write the notify-send part of the command every time
2.  I want to delete a specific reminder
3.  I want to show a list of all the reminders set

Point just 1 needs a wrapper, some easy script (I called it `rem`) that crafts the actual command line to pass to `at`.

For example the following:
```bash
$ cat rem
#!/usr/bin/env bash
echo "notify-send \"$@\""
```

Which I can then pass to `at` to set the reminder

```
$ rem buy the milk | at 5pm
```

Actually, not all *smart dates* are super easy in `at`. For example, if I want a reminder to fire in *30 minutes*, the syntax is

```
$ at now + 30 minutes
```

not bad, but what if I set `alias in="at now +"` in my `.bashrc`? Now it is much better:
```
$ rem buy the milk | in 30 minutes
```

So, back to the point, we can set any reminder now, but how to delete or list them? `at` is well equipped with `atq` and `atrm` commands.

- `atq` shows a list of the jobs with their ID and time
- `atrm` deletes a job by ID

```bash
$ atq
1       Mon Apr  1 17:57:00 2024 a carlo
$ atrm 1
```

This is already good and I don't feel the urge to write any wrapper around it.

However, `atq` it only shows the job, not the message, so I cannot see the reminder message associated.

This last requirements needs some more work. Basically looping over the jobs and extracting the message from the job content, but I had fun and pushed a little more into the script getting the message together with the time of execution and the time left.

```bash
$ rem
- Apr/13/2024 17:39/0h:17m (6) call dad
- Apr/13/2024 18:00/0h:38m (7) buy the milk
- Apr/14/2024 20:00/01d (5) take out the trash
```

You can see and use the resulting app at https://github.com/clobrano/rem.


**Bottom line**: Linux is full of useful utilities, and it is often enough just to combine them to get nice results and some fun.
