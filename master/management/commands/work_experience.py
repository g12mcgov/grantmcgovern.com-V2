#!/usr/bin/env python

# -*- coding: utf-8 -*-
#
# @Author: grantmcgovern
# @Date:   2015-07-05 20:30:13
# @Email:   me@grantmcgovern.com
# @Web:    http://grantmcgovern.com
#
# @Last Modified by:   grantmcgovern
# @Last Modified time: 2015-07-12 19:58:13


import sys
import logging
import requests

def task():
	global linkedin_logger
	linkedin_logger = configLogger('LinkedIn')
	response = LinkedIn.get_work_experience()
	LinkedIn.parse_work_experience(response)

class LinkedIn:
	url = 'https://api.linkedin.com/v1/people/~:(id,positions)'
	headers = { "Authorization": "AUTHORIZATION KEY WILL GO HERE" }
	data = { "format": "json", "scope": "r_fullprofile" }

	@classmethod
	def get_work_experience(self):
		linkedin_logger.info('Requesting LinkedIn...')
		response = requests.get(
			self.url, 
			headers=self.headers, 
			data=self.data
			)
		return response

	@classmethod
	def parse_work_experience(self, content):
		linkedin_logger.info('Parsing LinkedIn Data...')
		for experience in content:
			#
			# Extract work positions here.
			#
			pass 

def configLogger(name):
	""" 
	Sets up a logger for the entire application to use 
	"""
	logger = logging.basicConfig(
	stream=sys.stdout,
    level=logging.DEBUG, 
    format="%(asctime)s [ %(threadName)s ] [ %(levelname)s ] : %(message)s'", 
    datefmt='%Y-%m-%d %H:%M:%S' 
	)

	logger = logging.getLogger(name)

	return logger

## Debug ##
if __name__ == "__main__":
	task()
