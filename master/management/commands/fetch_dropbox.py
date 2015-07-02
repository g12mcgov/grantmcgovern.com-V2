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
