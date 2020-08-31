---
date: "2018-12-12T00:00:00Z"
excerpt: Extend VIM configuration per project
draft: false
share: true
tags:
- vim
- configuration
- vimscript
- linux
- macos
title: Per project VIM setting extension
---

Lately, it's been common for me to add per-project VIM commands. It's usually a simple thing, like adapting the `:make` command to the project structure, e.g. when the makefile is in some subdirectory

    nnoremap <leader>1 :make -C somedir
    
or

    nnoremap <leader>3 yaru-build.sh
    
:)

VIM remembers last commands when the session is closed, so re-setting this mapping every time is not much of a pain, but doing it again and again at last gets annoying.

The following is a very (I mean very) easy improvement of this use case.
I added at the end of my `.vimrc` (actually `init.vim`, since I usually use [neovim](https://neovim.io/)) the following command

    if filereadable(expand('vimrc.local'))
        exe 'source vimrc.local'
    endif

so that, if a project has a file called `vimrc.local` it is sourced, extending normal VIM configuration, if not, it fails silently.

If the project is under versioning and it's using GIT, you might want to add `vimrc.local` to *gitignore*. I suggest to use the global gitignore, to avoid sharing your personal gitignore configuration with the project.
