#
#
#   master/views.py
#
#   Author: Grant McGovern
#   Date: 27 June 2015
#
#   Personal Site V2
#
#   Contact: grantmcgov@gmail.com
#


## Module Imports
import json
import datetime

## Django Imports 
from django.shortcuts import render
from django.http import HttpResponse

## Import master models
from master.models import DevCharts

def index(request):
	# Grab latest DevCharts object
	devcharts_obj = DevCharts.objects.filter().latest('date')
	devcharts_data = {
	'languages': [item['language'] for item in devcharts_obj.data], 
	'counts': [item['files'] for item in devcharts_obj.data]
	}

	# print "\n\n\n"
	# print devcharts_obj.data
	# print "\n\n\n"

	print json.dumps(devcharts_data)
	return render(
		request, 
		'master/index.html', 
		{ "content": json.dumps(devcharts_data) }
		)