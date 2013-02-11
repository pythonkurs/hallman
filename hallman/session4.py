#!/usr/bin/env python

import requests
from dateutil import parser
from pandas import DataFrame


user = raw_input('Enter your user name: ')
password = raw_input('Enter your password: ')

users = requests.get("https://api.github.com/orgs/pythonkurs/members", auth=(user, password))
users_data = users.json()

repos = requests.get("https://api.github.com/orgs/pythonkurs/repos", auth=(user, password))
repo_data = repos.json()

for i in repo_data:
	commit_url = i[u'commits_url'][:-6]
	urls = requests.get(commit_url, auth=(user, password)) 
	url_data = urls.json()
	for ii in url_data:
		try:
			print ii[u'commit'][u'message']
			print ii[u'commit'][u'author'][u'date']
		except TypeError: print '200'

	

#parser.parse.now()

#with open("secret") as secret:
#	password = secret.read().strip()
