#!/usr/bin/env python

# -*- coding: utf-8 -*-
#
# @Author: grantmcgovern
# @Date:   2015-07-12 13:56:00
# @Email:   me@grantmcgovern.com
# @Web:    http://grantmcgovern.com
#
# @Last Modified by:   Grant McGovern
# @Last Modified time: 2016-10-12 22:49:43


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
	work_experiences = list(reversed(WorkExperience.objects.all()))
	# This is a terrible hacky fix to get the most recent work experience
	# object to show up first, this is because I was silly and neglected
	# to include a "date_created" field along with the model.
	work_experiences_names = [experience.position for experience in work_experiences]
	most_recent_index = work_experiences_names.index('Software Engineer (eCommerce)')
	most_recent = work_experiences[most_recent_index]
	work_experiences.pop(most_recent_index)
	work_experiences.insert(0, most_recent)

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