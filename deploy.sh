#!/usr/bin/env bash
# -*- coding: UTF-8 -*-
set -x
pwd
ls
cat .gitmodules
ls -l themes
git submodule init
git submodule update
ls -l themes
ls -l themes/*
hugo
