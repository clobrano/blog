---
title: "Git: A Silly Mnemonic for Squash"
date: 2025-11-28T16:53:15+01:00
draft: false
---

I always forget how to squash commits.

It should be a standard part of my workflow, but every time I need to clean up my history and combine a few commits, I never remember the process and since it might break badly, I freeze.

I finally wrote down a simple rule (and a mnemonic) to stop guessing.

### An example scenario

I was working on a feature and ended up with a messy log. I wanted to combine the "typo" and "linter" fixes into the main feature commit, but I had already started some new work on top.

Here is my `git log`:

```text
* 9a1b2c (HEAD) WIP: experimenting with new API  <-- LEAVE THIS ALONE
* 8f3a9b fix: typo in documentation              <-- SQUASH THIS
* 2c4e1d fix: linter error                       <-- SQUASH THIS
* 9b1a3f feat: add user authentication           <-- INTO THIS
* 7d2e1f refactor: database connection           <-- PARENT
```

I wanted to merge the middle fixes into `feat: add user authentication`.

### The Solution

My instinct clashes with the fact that **you don't have to use the hash of the commit you want to modify** (`9b1a3f`), but the one before 🤷.

The rule is: **Always pick the Parent.**

From now on, I will use the mnemonic **R.I.P. messy history** (Rebase Interactive Parent), hoping to remember it forever 💪.

```bash
# I want to modify 9b1a3f, so I rebase its PARENT (9b1a3f^)
git rebase -i 9b1a3f^
```

### The Editor

While `git log` shows commits from the newest to the olders, the interactive editor does the opposite 🫠. So I shall remember to squash **UP**.

```text
pick   9b1a3f feat: add user authentication
squash 2c4e1d fix: linter error
squash 8f3a9b fix: typo in documentation
pick   9a1b2c WIP: experimenting with new API
```

1.  **Pick** the oldest commit (the feature).
2.  **Squash** the commits below it.
3.  **Pick** the newer work at the end (so it stays safe).


It works on [fixup commits too!](https://git-scm.com/docs/git-commit/2.32.0)

It is a silly thing, but it saves me from looking up the syntax every single time.
