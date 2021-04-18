import datetime
import os

import requests
from dotenv import load_dotenv

def shape_url(zipcode, address, interval):	
	since_dt = datetime.datetime.now() - datetime.timedelta(minutes = interval)
	since = since_dt.strftime("%Y-%m-%dT%H:%m:00")
	
	url = "https://data.cityofnewyork.us/resource/erm2-nwe9.json?incident_zip={}&incident_address={}&$where=created_date >= '{}'"
	
	return url.format(zipcode, address, since)

def get_data(zipcode, address, interval):
	msg = ''
	url = shape_url(zipcode, address, interval)
	r = requests.get(url)
	data = r.json()
	if len(data) > 0:
		msg += ":rotating_light: **311 ALERT!** :rotating_light:\n{} new complaint(s) for {}\n".format(len(data), address)
		for complaint in data:
			id_ = complaint.get('unique_key')
			complaint_type = complaint.get('complaint_type')
			descriptor = complaint.get('descriptor')
			msg += '\nComplaint: {} - {}'.format(complaint_type, descriptor)
	return msg

def post_msg(msg):
	discord = os.getenv('DISCORD_URL')
	data = {'content': msg}
	x = requests.post(discord, data = data)
	print(x)

def run():
	load_dotenv()

	zipcode = os.getenv('ZIPCODE')
	address = os.getenv('ADDRESS')
	interval = int(os.getenv('INTERVAL'))

	msg = get_data(zipcode, address, interval)
	if msg != '':
		post_msg(msg)

run()
