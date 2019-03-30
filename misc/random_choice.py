import random
import sys
import csv

NUM_WINNERS = 3

if len(sys.argv) != 2:
	print("Please enter file location as first command line arg")
else:
	responders = []
	try:
		with open(sys.argv[1]) as csv_file:
			csv_reader = csv.DictReader(csv_file)
			for row in csv_reader:
				for (k,v) in row.items():
					if "drawing" in k:
						if v != "" and v not in responders and "Mihajlo" not in v and "Lucas" not in v:
							responders.append(v)
		responders.append("Rick Beltran")
		print("Winners are: ", random.sample(responders, 3))
	except:
		print("Bad file location")