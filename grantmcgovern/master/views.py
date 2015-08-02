#!/usr/bin/env python

# -*- coding: utf-8 -*-
#
# @Author: grantmcgovern
# @Date:   2015-07-12 13:56:00
# @Email:   me@grantmcgovern.com
# @Web:    http://grantmcgovern.com
#
# @Last Modified by:   grantmcgovern
# @Last Modified time: 2015-07-13 21:38:48


## Module Imports
import json
import datetime

## Django Imports 
from django.shortcuts import render
from django.http import HttpResponse

## Import master models
from master.models import DevCharts, WorkExperience

def index(request):
	# Grab latest DevCharts object
	devcharts_obj = DevCharts.objects.filter().latest('date')
	devcharts_data = {
	'languages': [item['language'] for item in devcharts_obj.data], 
	'counts': [item['files'] for item in devcharts_obj.data]
	}

	# Get all work experience objects (in chronological order)
	work_experiences = reversed(WorkExperience.objects.all())

	return render(
		request, 
		'master/index.html', 
		{
			"content": json.dumps(devcharts_data),
			"work_experiences": work_experiences
		})

def about(request):
	context_dict = {'temp': 'temp'}
	return render(request, 'master/about.html', context_dict)