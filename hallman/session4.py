#!/usr/bin/env python

import requests
import json
import getpass
from dateutil import parser
from pandas import DataFrame, Series


def gmcc(df):
	
	commits_day = df.count(1).resample("D", how='sum').fillna(0)
	sort_day = commits_day.index.dayofweek
	day = commits_day.groupby(sort_day).sum()
	week_list = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
	print 'The day is: %s' %week_list[day.idxmax()]
	
	commits_hour = df.count(1).resample("H", how='sum').fillna(0)
	sort_hour = commits_hour.index.hour
	hour = commits_hour.groupby(sort_hour).sum()
	max_hour = hour.idxmax()
	print 'The hour is: %d' %max_hour



def get_data():
	username = raw_input('Enter your user name: ')
	password = getpass.getpass('Enter your password: ')
	repos = requests.get("https://api.github.com/orgs/pythonkurs/repos", auth=(username, password))
	repo_data = repos.json()
	
	date_list = []
	message_list = []
	
	for i in repo_data:
		commit_url = i[u'commits_url'][:-6]
		urls = requests.get(commit_url, auth=(username, password)) 
		url_data = urls.json()
		for j in url_data:
			try:
				date = parser.parse(j[u'commit'][u'author'][u'date'])
				date_list.append(date)
				
				message = j[u'commit'][u'message']
				message_list.append(message)

			except TypeError:
				pass
				
	serie = Series(message_list, index = date_list, name = 'DataFrame')
	df = DataFrame(serie)
	return df



