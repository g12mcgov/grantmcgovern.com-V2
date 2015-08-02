#!/usr/bin/env python

# -*- coding: utf-8 -*-
#
# @Author: grantmcgovern
# @Date:   2015-07-12 14:17:45
# @Email:   me@grantmcgovern.com
# @Web:    http://grantmcgovern.com
#
# @Last Modified by:   grantmcgovern
# @Last Modified time: 2015-07-12 19:55:59


from django import forms
 
class StringListField(forms.CharField):
	"""
	Class to store list of work entries 
	"""
	def prepare_value(self, value):
		return ', '.join(value)

	def to_python(self, value):
		if not value:
			return []
		return [item.strip() for item in value.split(',')]