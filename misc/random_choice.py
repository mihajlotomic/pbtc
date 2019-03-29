import random
import argparse

NUM_WINNERS = 3

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--num_responses', type=int,
					help='Number of total survey respondents')
					
args = parser.parse_args()
			
if args.num_responses:		
	NUM_RESPONSES = args.num_responses
else:
	exit('Total number of survey respondents is missing')
	
random = random.Random()
for i in range(1, NUM_WINNERS+1):
	print('Winner Number {}: is {}'.format(i, round(random.uniform(2, NUM_RESPONSES+1))))