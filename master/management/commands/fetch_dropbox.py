#!/usr/bin/env python

# -*- coding: utf-8 -*-
#
# @Author: grantmcgovern
# @Date:   2015-07-01 23:13:26
# @Email:   me@grantmcgovern.com
# @Web:    http://grantmcgovern.com
#
# @Last Modified by:   grantmcgovern
# @Last Modified time: 2015-07-12 19:57:53


import datetime
## Local Imports
from devcharts import task as devcharts_task
## Django Imports
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
	"""
	Defines a command for fetching Dropbox file info
	"""
	args = None
	help = 'Fetches Dropbox API data for file extension computation'

	def handle(self, *args, **options):
		devcharts_task()
		self.stdout.write(
			'Successfully ran task at: ' 
			+ datetime.datetime.now().strftime("%A %Y-%m-%d %H:%M:%S")
			)
