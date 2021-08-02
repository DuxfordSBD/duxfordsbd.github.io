#!/usr/bin/env python3

import sys
import csv
import re
import os
from datetime import datetime, timedelta
from os import path
import json
import sqlite3

def normalise_name(name):
	normalised_name=re.sub(r'\s+', '_', name.lower())
	return normalised_name

# Find fastest stats for each person for a single route
def get_summary(cur, route):
	summary_sql='''select name, count(*) as runs, route, min(time(how_long)) as fastest_time from results where route =? group by name, route order by runs desc'''
	cur.execute(summary_sql, [route])
	rows = cur.fetchall()
	results=[]
	for row in rows:
		summary={}
		name=row[0]
		summary['normalised_name'] = normalise_name(name)
		summary['name'] = name
		summary['times_run'] = row[1]
		summary['route'] = row[2]
		summary['fastest_time'] = row[3]
		results.append(summary)
	return results

# Getting inputs
file=sys.argv[1]
summary={
	'adults' : {},
	'kids' : {}
}

# Create DB in memory
con = sqlite3.connect(':memory:')
cur = con.cursor()
cur.execute('''CREATE TABLE results
               (name text, dateofrun text, how_long text, age_group text, gender text, route text)''')
con.commit()

# Read CSV file in with columns
with open('_data/couch_to_soap_box_2021.csv', 'r') as fin:
	dr = csv.DictReader(fin)
	to_db = [(i['name'], i['dateofrun'], i['how_long'], i['age_group'], i['gender'], i['route']) for i in dr]

# Write the columns back out
cur.executemany('''INSERT into results (name, dateofrun, how_long, age_group, gender, route) VALUES (?,?,?,?,?,?)''', to_db)
con.commit()

# Start querying for the results
kids_summary=get_summary(cur, 'Off-road children’s route')
adults_summary=get_summary(cur, 'Full soap box derby route')

if kids_summary:
	summary['kids']['results'] = kids_summary
	summary['kids']['most'] = { "name" : kids_summary[0]['name'], 'times' : kids_summary[0]['times_run'] }
if adults_summary:
	summary['adults']['results'] = adults_summary
	summary['adults']['most'] = { "name" : adults_summary[0]['name'], 'times' : adults_summary[0]['times_run'] }

# # Setup target dir
results_csv_dir=path.join('.', '_data', 'c2sbd-2021')
if not path.exists(results_csv_dir):
	os.makedirs(results_csv_dir)

summary_json_file=path.join(results_csv_dir, 'summary.json')
with open(summary_json_file, 'w') as json_file:
	json.dump(summary, json_file, indent=2)

#### START WRITING OUT INVIDVIDUAL RESULTS FOR EACH ATHLETE
cur.execute('''select distinct(name) from results''')
names=cur.fetchall()
for row in names:
	name=row[0]
	normalised_name=normalise_name(name)
	target_md_file = '{}.md'.format(normalised_name)
	target_csv_file = '{}.csv'.format(normalised_name)
	cur.execute('''select dateofrun, time(how_long) as timetaken, route from results where name =? order by timetaken asc ''', [name])
	results=cur.fetchall()
	csv_file=path.join(results_csv_dir, target_csv_file)
	with open(csv_file, 'w') as csvfile:
		csvwriter = csv.writer(csvfile)
		csvwriter.writerow(['date', 'time', 'route'])
		for result in results:
			csvwriter.writerow(result)
	fastest_time=results[0][1]

	# Write out the markdown file for each athlete
	results_md_dir=path.join('.', 'couch_to_soap_box_derby', '2021')
	target_md_file=path.join(results_md_dir, target_md_file)
	if not path.exists(results_md_dir):
		os.makedirs(results_md_dir)
	with open(target_md_file, 'w') as mdfile:
		##### NB: MAKE SURE INDENTATION HERE IS IN SPACES. OTHERWISE YAML DOES NOT PARSE
		template="""---
layout: couchtosoapboxderby-individual-results
header:
  image_fullwidth: duxford-soapbox-derby-header.jpg
athlete: {}
title: "2021 Couch to Soap Box Derby results for {}"
datatables: 
  - 
    id: results
    sort_column:
      column: 1
      order: asc
fastest_time: '{}'
---
"""
		mdfile.write(template.format(normalised_name,name,fastest_time))
