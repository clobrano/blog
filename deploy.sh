#!/usr/bin/env bash
# -*- coding: UTF-8 -*-
set -x
pwd
ls
cat .gitmodules
ls -l themes
echo "Init submodules"
git submodule init
git submodule update --force --recursive --init --remote
echo "---"
ls -l themes
ls -l themes/*
hugo --gc --minify
