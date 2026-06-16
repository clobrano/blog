---
title: "I Built Telekube"
date: 2026-06-16T10:47:35+02:00
draft: false
---


I built [telekube](https://github.com/clobrano/telekube), a terminal UI for Kubernetes clusters.

Pretty straightforward motivation: I was constantly inspecting the same resources, usually in the same namespaces: pods, deployments, services. Finding a resource name meant typing the same commands over and over, or relying on aliases. Got annoying fast.

The idea was simple: save each command in a different tab. Switch between them throughout the day, find what you need, done. Once listing resources became easy, the rest followed naturally. You can describe, view logs, filter, sort by any column. Each feature made sense as an extension of the core idea.

It's not complicated, but it removes friction. Instead of typing `kubectl get pods -n myns | grep foo`, you just have a tab with that view, hit `j` and `k` to move around, press `d` to describe the instance, or `L` to see the logs; many commands are covered.

```sh
telekube  # just run it
```

If you're tired of retyping the same kubectl commands, might save you some time.
