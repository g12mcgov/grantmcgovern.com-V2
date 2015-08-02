#!/usr/bin/env python

# -*- coding: utf-8 -*-
#
# @Author: grantmcgovern
# @Date:   2015-07-16 22:20:06
# @Email:   me@grantmcgovern.com
# @Web:    http://grantmcgovern.com
#
# @Last Modified by:   grantmcgovern
# @Last Modified time: 2015-07-16 22:29:08


import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

## Get our requirements from our .txt file
with open('requirements.txt') as requirements:
	modules = [line.strip('\n') for line in requirements]
	for line in modules:
		print line

setup(
    name='grantmcgovern.com-v2',
    version='0.1',
    install_requires=modules,
    include_package_data=True,
    license='MIT License',  # example license
    description='My personal website.',
    long_description=README,
    url='http://www.grantmcgovern.com/',
    author='Grant McGovern',
    author_email='me@grantmcgovern.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Recruiters',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)