---
title: "Extend Mkdir"
date: 2022-03-17T16:51:53+01:00
draft: false
---


# Let mkdir create parents directories

I noticed that it is more than a year since the last post, so I thought that a small new content would have been easier to write.
This in particular refers to an extension I wrote some time ago for the `mkdir` system call to make it a bit more proactive :smile:.

90% of the times, I use `mkdir` to create a new folder in the current directory, so the few times I want to create a new folder in a deeper path I always forget to add the `--parent` flag.

```sh
me/blog $ mkdir foo/bin/bar
mkdir: cannot create directory ‘foo/bin/bar’: No such file or directory
```

as the [Man-pages](https://man7.org/linux/man-pages/man1/mkdir.1.html) would tell you, since the parent directory `foo/bin` does not exist, `mkdir` fails to create `bar`, but what if `mkdir` were so kind to tell me just that, and suggests to add the flag on my behalf? :smile:

This is actually somehow easy.

First of all, you need a way to define new functions in your shell. I use **zsh**, but in **bash** would be the same: write a function definition in a file and source it in _.bashrc_ or _.zshrc_.

This comes from my _.zshrc_
```sh
#
# Functions and aliases
#
source ~/.dot/.config/cconf/zsh/functions.zsh
```
What to do for `mkdir`?

1. override it with a custom function :arrow_right: `function mkdir() {}`
2. find the parent directory `mkdir` expects to exist already :arrow_right: `echo $1 | grep -E -q '[\S+/]+'`
3. if it doesn't exist, ask if it must be created or not :arrow_right: `echo "Press ENTER to run mkdir with --parents."`

Ok, point 2 probably requires some explaination, so let's back to the example above

```sh
me/blog $ mkdir foo/bin/bar
```

`bar` is the folder to be created, while `foo/bin/` is the parent.
The `grep` expression above looks for any sequence of substrings ending with slash `/`: `foo/`, `foo/bar/`, etc., but not `bar`, or `foo`, which would be a directory in the _current_ folder.

So putting all these pieces together:
```sh
function mkdir() {
    # extend mkdir with custom features
    # propose adding "--parents" flag.
    echo $1 | grep -E -q '[\S+/]+'
    if [[ $? == 0 && ! -d $1 ]]; then
        # one of the directories in $1 path do not exist
        # suggest adding "--parents" flag.
        echo "# Some parents in $1 do not exist. Press ENTER to run mkdir with --parents."
        read
        command mkdir --parents $@
        echo "# done"
    else
        command mkdir $@
    fi
}
```

Let's try again

```sh
me/blog $ mkdir foo/bin/bar                                                                                    
# Some parents in foo/bin/bar do not exist. Press ENTER to run mkdir with --parents.

# done

me/blog $ tree | grep -e foo -e bar -e bin
├── foo
│   └── bin
│       └── bar
```
Of course in a similar manner you can override `rm` as well (see [here](https://github.com/clobrano/dot/blob/master/.config/cconf/zsh/functions.zsh#L21)).
