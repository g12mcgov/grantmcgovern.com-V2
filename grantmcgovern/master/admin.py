#!/usr/bin/env python

# -*- coding: utf-8 -*-
#
# @Author: grantmcgovern
# @Date:   2015-07-12 15:42:46
# @Email:   me@grantmcgovern.com
# @Web:    http://grantmcgovern.com
#
# @Last Modified by:   grantmcgovern
# @Last Modified time: 2015-07-12 21:20:40


from django.contrib import admin
from models import WorkExperience
from django.contrib.admin import site, ModelAdmin

def summary(instance):
    return ', '.join(instance.summary)

class WorkExperienceAdmin(ModelAdmin):
	list_display = ['summary', summary]

admin.site.register(WorkExperience, WorkExperienceAdmin)