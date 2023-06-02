+++
title = "Curious Bash: Get Notified When It's Done"
date = 2023-06-02T15:28:58+02:00
tags = ["bash", "automation"]
draft = false
+++

Bash scripting is a powerful tool that allows you to automate various tasks on your computer. One common scenario is running time-consuming processes and wanting to be notified when they are completed. Many resources explain how to write a bash script that sends a notification when a process finishes. However, if you're like me, you might forget to append the necessary call to [`notify-send`](https://manpages.org/notify-send).

In this post, I'll share a script that not only sends a notification when a process finishes but also finds the running process and waits for its completion before triggering the notification.

### Finding the Running Process

To find the running process, we can search for a process with a given command line. Fortunately, the `/proc` filesystem keeps the command line that started each process, allowing us to use the [`pgrep`](https://www.man7.org/linux/man-pages/man1/pkill.1.html) command:

```
$ pgrep make
86379
```

To ensure accuracy, let's add some additional checks. Create a file named `when-done.sh` and add the following content:

```sh
query=$1
pid=$(pgrep "${query}")

occurrences=$(echo "${pid}" | wc -w)
if [[ ${occurrences} -eq 0 ]]; then
    echo "[!] No matching process for this query."
    exit 1
fi
if [[ ${occurrences} -gt 1 ]]; then
    echo "[!] found too many (${occurrences}) matching processes. Use a more specific query"
    exit 1
fi

# Read the process' command line
cmd=$(cat /proc/${pid}/cmdline | sed -e "s/\x00/ /g"; echo)
echo "Got PID: \"${pid}\" for query: \"${query}\", with cmdline: \"${cmd}\""
echo "Confirm?"
read
```

Let's test it:

```
$ ./when-done.sh make
Got PID: "100822" for query: "make", with cmdline: "make death-star-with-chatgpt "
Confirm?
```

It seems to be working fine! :smile: Now, let's add some final details.

### Waiting for the Process to Complete

```sh
query=$1
pid=$(pgrep "${query}")

[...]

# Read the process' command line
cmd=$(cat /proc/${pid}/cmdline | sed -e "s/\x00/ /g"; echo)
echo "Got PID: \"${pid}\" for query: \"${query}\", with cmdline: \"${cmd}\""
echo "Confirm?"
read
echo "Let's wait for it"
tail --pid=${pid} --follow /dev/null
```

Great! We can use the [`tail`](https://www.man7.org/linux/man-pages/man1/tail.1.html) command to wait for a process to die.

That's it! When your long-running process has started, you can wait for its completion and be notified by using the following command:

```sh
when-done.sh make && notify-send "I'm done, master!"
```

The full script is available [here](https://github.com/clobrano/script-fu/blob/master/when-done.sh).

### Bonus

If you prefer to be notified on your mobile phone while leaving your PC, you can check out https://ntfy.sh. :wink:
