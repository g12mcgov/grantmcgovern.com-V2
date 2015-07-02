web: gunicorn --log-file=- grantmcgovern.wsgi:application NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program command options
worker: python tasks/devcharts.py
