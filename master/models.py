#!/usr/bin/env python

# -*- coding: utf-8 -*-
#
# @Author: grantmcgovern
# @Date:   2015-07-12 15:35:28
# @Email:   me@grantmcgovern.com
# @Web:    http://grantmcgovern.com
#
# @Last Modified by:   grantmcgovern
# @Last Modified time: 2015-07-15 22:49:51


import datetime
from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField

# Local Imports
from .forms import StringListField

class WorkSummary(ListField):
	"""
	Intermediary class so ListField can be displayed in Django Admin
	"""
	def formfield(self, **kwargs):
		return models.Field.formfield(self, StringListField, **kwargs)

class DevCharts(models.Model):
	"""
	Model to store Dropbox API info
	"""
	date = models.DateTimeField(default=datetime.datetime.now())
	data = ListField()

class WorkExperience(models.Model):
	"""
	Model to store Work Experience entry 
	"""
	company = models.CharField(max_length=30)
	position = models.CharField(max_length=80)
	slug = models.SlugField(unique=True)
	summary = models.TextField() #WorkSummary()
	image = models.ImageField(upload_to='master')
	location = models.CharField(max_length=30)
	daterange = models.CharField(max_length=30)
	url = models.URLField()

	def summary_to_list(self):
		"""
		Django admin causes an arbitrary unicode character, 
		`\r` to be inserted on line breaks. This filters 
		those out.
		""" 
		return filter(lambda element: element != u'\r', self.summary.split('\n'))
