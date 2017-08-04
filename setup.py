#!/usr/bin/env python

import os
from setuptools import setup


version = '0.0.1'
try:
    with open('VERSION'), 'r') as fid:
        version = fid.read().strip()
except:
    pass


setup(
    name='pygts',
    version=version,
    description='PyGTS: GTS Python3 Wrapper',
    packages=['pygts'])
