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
import datetime

## Django Imports 
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	message = {"hey": "yo"}
	return render(request, 'master/index.html', message)