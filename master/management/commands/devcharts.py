import os
import sys
import json
import pymongo
import dropbox
import logging
import datetime
import ConfigParser
from collections import Counter
from pathos.multiprocessing import ProcessingPool

## Import master models
from master.models import DevCharts

## Config.cfg file path
CONFIG_PATH = os.path.join(
	os.path.dirname(os.path.realpath(__file__)), 'config.cfg'
	)

def task():
	"""
	MAIN
	"""
	global db
	global global_logger

	global_logger = configLogger('global')
	auth = getkeys()

	# try:
	# 	# Instantiate Mongo client
	# 	client = pymongo.MongoClient(auth['mongo_host'], auth['mongo_port'])
	# 	db = client.heroku_87fdg4b3
	# 	try:
	# 		db.authenticate(auth['mongo_user'], auth['mongo_password'])
	# 		global_logger.info('Successfully authenticated w/ MongoDB...')
	# 	except:
	# 		raise Exception('Could not authenticate MongoDB') 
	# 	global_logger.info('Successfully established MongoDB connection...')
	# except pymongo.errors.ConnectionFailure as err:
	# 	raise err

	dropbox = Dropbox(
		auth['key'], 
		auth['secret'], 
		auth['token'], 
		auth['userid']
		)

	dropbox.analyze('/Developer/Projects')

class Dropbox:
	def __init__(self, key, secret, *args):
		"""
		Instantiates the Dropbox API
		"""
		# Hold client connection
		self.client = ''
		self.logger = configLogger('devcharts')
		self.directory = '/Developer/Projects'

		if key and secret and len(args) == 2:
			self.token = args[0]
			self.userid = args[1]
			self.connect(self.token, self.userid)
		elif len(args) > 2:
			raise Exception(
				"Too many arguments"
				)
		else:
			self.authorize(key, secret)

	def authorize(self, key, secret):
		"""
		Authorizes against Dropbox API
		"""
		self.logger.info('Authorizing...')
		flow = dropbox.client.DropboxOAuth2FlowNoRedirect(key, secret)
		authorize_url = flow.start()
		
		print '1. Go to: ' + authorize_url
		print '2. Click "Allow" (you might have to log in first)'
		print '3. Copy the authorization code.'
		
		self.code = raw_input("Enter the authorization code here: ").strip()
		self.access_token, self.user_id = flow.finish(self.code)
		
		print self.access_token
		print self.user_id

	def connect(self, token, userid):
		"""
		Connects to Dropbox
		"""
		self.logger.info('Establising Dropbox connection...')
		self.client = dropbox.client.DropboxClient(token)

	def info(self):
		"""
		Returns Dropbox client info
		"""
		return client.account_info()
	
	def analyze(self, directory):
		"""
		Creates a pool of multiprocessing workers used to search
		"""
		self.logger.info('Analyzing Directory: %s', str(directory))
		#pool = ProcessingPool(1)
		
		extensions = [
		'.py', 
		'.js', 
		'.cpp', 
		'.css', 
		'.html',
		'.erl',
		'.java',
		'.plg',
		'.rb',
		'.c',
		'.h',
		'.hpp',
		'.cc',
		'.php',
		'.less',
		'.sass',
		'.asm',
		'.s',
		'.sh',
		'.bash',
		'.go',
		'.swift',
		'.coffee',
		'.maple',
		'.matlab',
		'scala'
		]

		# Compute breakdowns
		breakdown = []
		for extension in extensions:
			result = self.search(extension)
			# Only care about find results w/ a count > 0
			if not result['files']:
				breakdown.append(result)

		print breakdown
		#breakdown = pool.map(self.search, extensions)
		distribution = self.compute(breakdown)
		insert(distribution)

	def search(self, extension):
		"""
		Searches Dropbox directory for file extensions
		"""
		self.logger.info('Searching: ' + str(extension))
		files = self.client.search(
			self.directory, 
			extension, 
			file_limit=1000, 
			include_deleted=False
			)

		return {
		'extension': extension,
		'files': len(files),
		'language': self.tag(extension) 
		}


	def prettyprint(self, content):
		"""
		Pretty prints JSON
		"""
		print json.dumps(content, separators=(',',':'), indent=4)

	def compute(self, languages):
		"""
		Computes percentage distribution of each language
		"""
		total = sum([count['files'] for count in languages])
		for language in languages:
			language['percentage'] = (language['files'] / float(total))
		return languages

	def tag(self, extension):
		"""
		Tags each extension with the corresponding language
		"""
		self.logger.info('Tagging Extension: ' + str(extension))
		if extension == '.py':
			return 'Python'
		elif extension == '.js':
			return 'JavaScript'
		elif extension == '.cpp' or extension == '.hpp' or extension == '.cc' or extension == '.h':
			return 'C++'
		elif extension == '.css' or extension == '.less' or extension == '.sass':
			return 'CSS'
		elif extension == '.html':
			return 'HTML'
		elif extension == '.erl':
			return 'Erlang'
		elif extension == '.scala':
			return 'Scala'
		elif extension == '.java':
			return 'Java'
		elif extension == '.plg':
			return 'Prolog'
		elif extension == '.rb':
			return 'Ruby'
		elif extension == '.c' or extension == '.h':
			return 'C'
		elif extension == '.php':
			return 'PHP'
		elif extension == '.asm' or extension == '.s':
			return 'Assembly'
		elif extension == '.sh' or extension == '.bash':
			return 'Shell'
		elif extension == '.go':
			return 'Go'
		elif extension == '.swift':
			return 'Swift'
		elif extension == '.m':
			return 'Objective-C'
		elif extension == '.coffee':
			return 'Coffeescript'
		elif extension == '.maple':
			return 'Maple'
		elif extension == '.matlab':
			return 'Matlab'
		else:
			return 'Other'

def insert(content):
	schema = { 
	'data': content,
	'date': datetime.datetime.now().strftime("%A %Y-%m-%d %H:%M:%S")
	}

	print json.dumps(content, separators=(',',':'), indent=4)

	try:
		new_devchart_entry = DevCharts.objects.create(
			data=schema['data']
			)
		
		new_devchart_entry.save()
		global_logger.info('Query Insert, Ok.')
	except pymongo.errors.OperationFailure as err:
		raise err

def merge(languages, counts):
	i = 0
	assert(len(languages) == len(counts))
	for i, (language, count) in enumerate(zip(languages, counts)):
		# Duplicates, merge
		if languages[i] == languages[i+1]:
			print language

def getkeys():
	"""
	Get the config file info
	"""
	parser = ConfigParser.RawConfigParser()
	parser.readfp(open(CONFIG_PATH))
	key = parser.get('dropbox', 'key')
	secret = parser.get('dropbox', 'secret')
	token = parser.get('dropbox', 'access_token')
	userid = parser.get('dropbox', 'user_id')
	mongo_host = parser.get('mongodb', 'MONGO_HOST')
	mongo_port = int(parser.get('mongodb', 'MONGO_PORT'))
	mongo_user = parser.get('mongodb', 'MONGO_USER')
	mongo_password = parser.get('mongodb', 'MONGO_PASSWORD')

	return {
	'key': key, 
	'secret': secret,
	'token': token,
	'userid': userid,
	'mongo_host': mongo_host,
	'mongo_port': mongo_port,
	'mongo_user': mongo_user,
	'mongo_password': mongo_password
	}

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

if __name__ == "__main__":
	task()
