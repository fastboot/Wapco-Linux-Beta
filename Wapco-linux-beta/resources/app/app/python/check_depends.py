#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from importlib import import_module
import sys

depends = ['requests', 'datetime', 'tzlocal', 'oauth2client', 'googleapiclient.discovery']

for mod in depends:
    try:
        mod = import_module(mod)
    except ModuleNotFoundError as e:
        print('Please install the following required Python modules:', depends, file=sys.stderr, flush=True)
        exit(1)
