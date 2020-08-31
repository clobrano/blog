---
date: "2014-06-08T00:00:00Z"
draft: false
excerpt: null
share: true
tags:
- openshift
- ssh
- security
title: Openshift and SSH Keys
---

Since I moved back to Ubuntu-based machines I had some "problems" with Openshift application management (I am talking about command line).
As you can read [here](/blog/post/1/), I use Openshift to host this blog and if until I worked on a Fedora machine everything was fine, on Ubuntu-based machines has totally been another story.

**This is totally my fault**, since I never had time/will to check what is wrong whity my usage of `rhc` client, but I just decided to change that.

The starting point is an application (this blog) already on the server and up and running. If the application has been created to the same machine you are working at the time you want modify something it's fine, because `rhc` client created the SSH keys you need (that you **really** need). But what if you changed machine? Well, it turned out to be pretty simple (my bad to have waisted so much time)!

**We have two steps**

## On client side

1. Generate a new pair of ssh keys<a rel="nofollow" href="#footnote1" id="ref_footnote1"><sup>1</sup></a>. I suggest to run the command directly `.ssh` folder.

{{< highlight bash >}}
$ssh-keygen -t rsa -C "your.email@yourprovider.com"
{{< / highlight >}}

2. Add your new key to the ssh-agent

{{< highlight bash >}}
$ssh-add id_rsa  # id_rsa is the *default* key's name.
{{< / highlight >}}

3. [optional] Move your keys into a `.ssh` subfolder. If and only if you do so, you also need to create a `config` file to let the ssh client know which keys are for which host.

{{< highlight bash >}}
$mv id_rsa* ~/.ssh/openshift
$vim config  # write something like the following

1 Host <application-name>.rhcloud.com
2     Hostname <application-name>.rhcloud.com
3     PreferredAuthentications publickey
4     IdentityFile ~/.ssh/openshift/id_rsa

$sudo service ssh restart  # Let the client know about the changes (I am not sure it is needed).
{{< / highlight >}}

## On Openshift side

1. Go to your application setting page
2. Click on `Add a new key...` button
3. Copy your `~/.ssh/openshift/id_rsa.pub` into the given box
4. Test connection: Check `Want to log in to your application?` link in your application page. Click on it and copy the ssh command, then execute it on your shell, adding the option **-vvv**

{{< highlight bash >}}
$ ssh -vvv ...
{{< / highlight >}}

The following line should appear

    debug1: Offering RSA public key: <your-home>/.ssh/openshift/id_rsa

and you'll be logged into your application. Just type `exit` before do something wrong :)

And that's it! I can now clone and modify and the rest.


#### References

* [GitHub Help](https://help.github.com/articles/generating-ssh-keys)

#### Footnotes
1. You are supposed to already have a pair of files named *id_rsa* on your `.ssh` folder. If your `id_rsa.pub` file is something like `ssh-rsa` followed by a bunch of characters, you can use that whithout generating a new pair.<a rel="nofollow" href="#ref_footnote1" id="footnote1">[↩]</a>.
