import datetime
from django.db import models
from djangotoolbox.fields import ListField

class DevCharts(models.Model):
	"""
	Model to store Dropbox API info
	"""
	date = models.DateTimeField(default=datetime.datetime.now())
	data = ListField()
	