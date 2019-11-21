import requests
from datetime import datetime
import csv
import os

class HttpPoster:
	PROTOCOL="HTTP"
	POST_TIME=None
	RESPONSE_TIME=None
	RESULTS_FILE="results/results.csv"
	def __init__(self, url, data, file_name, iteration):
		self.url = url
		self.data = data
		self.file_name = file_name
		self.iteration = iteration
		print("HTTP/POST iteration number %d starting..." % (self.iteration))
		pass
	def post(self):
		self.POST_TIME = datetime.now()
		print("Posting data to http server: %s" % (self.POST_TIME))
		response = requests.post(self.url, data=self.data)
		self.RESPONSE_TIME = datetime.now()
		print("Received response from http server code: %d at %s\n" % (response.status_code, self.RESPONSE_TIME))
		duration = self.RESPONSE_TIME - self.POST_TIME
		duration_micro=duration.microseconds
		print("Elapsed time: %s microseconds" % (duration_micro))
		self.write_results(os.stat(self.file_name).st_size, duration_micro, self.file_name, self.iteration)
	def write_results(self, file_size, duration_micro, size_name, iteration):
		print("Writing results for posting %s to %s\n" % (self.file_name, self.RESULTS_FILE))
		with open(self.RESULTS_FILE, 'a') as csvFile:
			writer = csv.writer(csvFile)
			writer.writerow([self.PROTOCOL, file_size, duration_micro, size_name, iteration])
		csvFile.close()