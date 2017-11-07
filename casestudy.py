"""
Imports:
- requests - call the API via HTTP and parse JSON response (incl json.loads)
             (could have used urllib, but...)
- datetime - manipulate unix timestamps into things we can read
"""
import requests
from datetime import datetime

#send GET to dummy JSON API I set up, could replace other API if working
r = requests.get('https://my-json-server.typicode.com/andrewbt/testjson3/stamps')

#use requests JSON method to convert text of API response to python list
stamps_list = r.json()

#Case Study Q #1: How many commits have we made?
#use python list len() function to count commits
print ("You've made " + str(len(stamps_list)) 
	+ " commits to the repo at " + r.url)

#Case Study Q #2: When did we stop updating this file?

#First, sort the list with Python list sorted() function
#In descending order to have 0'th element be most recent timestamp
stamps_list_sorted = sorted(stamps_list, reverse=True)

#Function to convert unix epoch to readable time, credit stackoverflow
#https://stackoverflow.com/questions/20512019/sorting-a-list-of-unix-time-stamp-values
#modified for American time though :)
def humanize_unixtime(unix_time):
    time = datetime.fromtimestamp(int(unix_time)).strftime('%m-%d-%Y %H:%M')
    return time

# A #2: When did we stop updating this file?
print "You stopped updating the file at " + humanize_unixtime(stamps_list_sorted[0])
