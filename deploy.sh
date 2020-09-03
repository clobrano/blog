#!/usr/bin/env bash
# -*- coding: UTF-8 -*-
set -x
pwd
ls
git submodule init
git submodule update
hugo
