#!/usr/bin/env python3

import sys
import csv
import re
from datetime import datetime, timedelta

file=sys.argv[1]
summary={}

with open(file) as csvfile:
	results = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in results:
		if 'Who are you' in row[0]:
			continue
		name=row[0]
		route=row[1]
		time=row[2]
		date=row[3]
		if name not in summary:
			summary[name] = {}
			summary[name]['results'] = []
			summary[name]['name'] = name
			summary[name]['target_file'] = 'pages/couch/2021/{}.html'.format(re.sub(r'\s+', '_', name.lower()))
		entry = {'route':route, 'time':time, 'date':date}
		pt = datetime.strptime(time, '%H:%M:%S')
		entry['parsed_time'] = timedelta(hours=pt.hour, minutes=pt.minute, seconds=pt.second)
		entry['parsed_date'] = datetime.strptime(date+'-2021', '%d-%b-%Y')
		summary[name]['results'].append(entry)

for athlete in summary:
	fastest_time=timedelta(hours=24)
	for entry in summary[athlete]['results']:
		if entry['parsed_time'] < fastest_time:
			fastest_time = entry['parsed_time']
	summary[athlete]['fastest_time'] = fastest_time

for key in summary:
	athlete=summary[key]
	print('{} - {}'.format(athlete['name'], athlete['fastest_time']))

print(summary)

