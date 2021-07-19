#!/usr/bin/env python3

import sys
import csv
import re
import os
from datetime import datetime, timedelta
from os import path
import json

# Formatting code taken from https://gist.github.com/thatalextaylor/7408395
def pretty_time_delta(seconds):
	sign_string = '-' if seconds < 0 else ''
	seconds = abs(int(seconds))
	days, seconds = divmod(seconds, 86400)
	hours, seconds = divmod(seconds, 3600)
	minutes, seconds = divmod(seconds, 60)
	if days > 0:
		return '%s%02dd%02dh%02dm%02ds' % (sign_string, days, hours, minutes, seconds)
	elif hours > 0:
		return '%s%02dh%02dm%02ds' % (sign_string, hours, minutes, seconds)
	elif minutes > 0:
		return '%s%02dm%02ds' % (sign_string, minutes, seconds)
	else:
		return '%s%02ds' % (sign_string, seconds)

# Getting inputs
file=sys.argv[1]
summary={}

# Read input CSV file
with open(file) as csvfile:
	results = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in results:
		if 'Who are you' in row[0]:
			continue
		name=row[0]
		route=row[1]
		time=row[2]
		date=row[3]
		age_group=row[4]
		gender=row[5]

		if name not in summary:
			summary[name] = {}
			summary[name]['results'] = []
			summary[name]['name'] = name
			summary[name]['age_group'] = age_group
			summary[name]['gender'] = gender
			summary[name]['route'] = route
			# Create a HTML & CSV filename, which can be used to create a summary for the athlete
			normalised_name=re.sub(r'\s+', '_', name.lower())
			summary[name]['normalised_name'] = normalised_name
			summary[name]['target_md_file'] = '{}.md'.format(normalised_name)
			summary[name]['target_csv_file'] = '{}.csv'.format(normalised_name)
		entry = {'route':route, 'time':time, 'date':date}
		# Parse submitted time, then create a timedelta to do duration comparison
		pt = datetime.strptime(time, '%H:%M:%S')
		entry['parsed_time'] = timedelta(hours=pt.hour, minutes=pt.minute, seconds=pt.second)
		entry['parsed_date'] = datetime.strptime(date+'-2021', '%d-%b-%Y')
		summary[name]['results'].append(entry)

# Find each athlete's fastest time
for athlete in summary:
	# Assume everyone will be faster than 24hrs
	fastest_time=timedelta(hours=24)
	for entry in summary[athlete]['results']:
		if entry['parsed_time'] < fastest_time:
			fastest_time = entry['parsed_time']
	summary[athlete]['fastest_time'] = fastest_time
	summary[athlete]['pp_fastest_time'] = pretty_time_delta(fastest_time.total_seconds())
	summary[athlete]['times_run'] = len(summary[athlete]['results'])

# Setup target dir
results_csv_dir=path.join('.', '_data', 'c2sbd-2021')
if not path.exists(results_csv_dir):
	os.makedirs(results_csv_dir)

# Write out the top level summaries to JSON
summary_json_file=path.join(results_csv_dir, 'summary.json')
json_summary={ 
	'adults': { 'results' : [], 'most': {'name' : '-', 'times': 0}, 'fastest' : { 'name': '-', 'time': '-'} }, 
	'kids': { 'results' : [], 'most': {'name' : '-', 'times': 0},'fastest' : { 'name': '-', 'time': '-'} }, 
}

adults = filter(lambda n: n['route'] == 'Adult', summary.values())
kids = filter(lambda n: n['route'] == 'Kids', summary.values())
most_run_adults = sorted(adults, key=lambda athlete: athlete['times_run'], reverse=True)
most_run_kids = sorted(kids, key=lambda athlete: athlete['times_run'], reverse=True)
fastest_adults = sorted(adults, key=lambda athlete: athlete['pp_fastest_time'], reverse=False)
fastest_kids = sorted(kids, key=lambda athlete: athlete['pp_fastest_time'], reverse=False)

# Update summaries
if adults:
	json_summary['adults']['most'] = { 'name': most_run_adults[0]['name'], 'times': most_run_adults[0]['times_run'] }
	json_summary['adults']['fastest'] = { 'name': most_run_adults[0]['name'], 'times': most_run_adults[0]['times_run'] }
if kids:
	json_summary['kids']['most'] = { 'name': most_run_adults[0]['name'], 'times': most_run_adults[0]['pp_fastest_time'] }
	json_summary['kids']['fastest'] = { 'name': most_run_adults[0]['name'], 'time': most_run_adults[0]['pp_fastest_time'] }

for athlete in sorted(summary.values(), key=lambda athlete: athlete['times_run']):
	if athlete['route'] == 'Adult':
		summary_key = 'adults'
	else:
		summary_key = 'kids'

	json_summary[summary_key]['results'].append({
		"name" : athlete['name'], 
		"normalised_name": athlete['normalised_name'], 
		"route" : athlete['route'], 
		"times_run" : athlete['times_run'], 
		"fastest_time" : athlete['pp_fastest_time']
	})

with open(summary_json_file, 'w') as json_file:
	json.dump(json_summary, json_file, indent=2)

# Write out summaries for each athlete (individual page and results CSV)
for key in summary:
	athlete=summary[key]
	#print('{} - {}'.format(athlete['name'], athlete['fastest_time']))
	
	# Write out each athlete's CSV file
	csv_file=path.join(results_csv_dir, athlete['target_csv_file'])
	with open(csv_file, 'w') as csvfile:
		csvwriter = csv.writer(csvfile)
		csvwriter.writerow(['date', 'time', 'route'])
		for result in athlete['results']:
			print(result)
			csvwriter.writerow([result['parsed_date'], result['parsed_time'], result['route']])
	
	# Write out the markdown file for each athlete
	results_md_dir=path.join('.', 'couch_to_soap_box_derby', '2021')
	target_md_file=path.join(results_md_dir, athlete['target_md_file'])
	if not path.exists(results_md_dir):
		os.makedirs(results_md_dir)
	with open(target_md_file, 'w') as mdfile:
		template="""---
layout: couchtosoapboxderby-individual-results
header:
  image_fullwidth: duxford-soapbox-derby-header.jpg
athlete: {}
title: "2021 Couch to Soap Box Derby results for {}"
datatables: 
  - results
fastest_time: {}
---
"""
		mdfile.write(template.format(athlete['normalised_name'], athlete['name'], athlete['pp_fastest_time']))

# print(summary)
