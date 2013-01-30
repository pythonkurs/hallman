#!/usr/bin/env python

import untangle
import requests

def getting_data():
	url= "http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml"
	data = requests.get(url).text
	
	doc = untangle.parse(data)
	outages = doc.NYCOutages.outage
	number = len(outages)
	count = 0
	for outage in outages:
		if outage.reason.cdata == 'REPAIR':
			count = count + 1
	ratio = count/float(number)
	print 'Fraction of outages caused by repair: ' + str(ratio)