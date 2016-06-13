# strip_the_html.py

import sys
import os
import re
import csv
import shutil

if not len(sys.argv) > 3:
    print '\nERROR: incorrect number of inputs\nusage: python stripHTML.py inputCSV outputCSV columns\nexample: python stripHTML.py messy_html.csv stripped.csv 4 5\n'
    exit()
       
### VARIABLES NEEDED FOR THE process_the_data function, which uses the strip_html function of MLStripper class
csvFile = sys.argv[1] # must be a csv, will be passed as a string
output = sys.argv[2]
column = map(int,list(sys.argv[3:])) # not sure how to pass this (as a string) to correctly index the data, see note in process_the_html function below

if not os.path.isfile(csvFile):
    print '\nERROR: input file not found \n' + \
    'usage: python stripHTML.py inputCSV outputCSV columns\n' + \
    'example: python stripHTML.py messy_html.csv stripped.csv 4 5\n'
    exit()

if not output.endswith('.csv'):
    print '\nERROR: output terms poorly contructed \n' + \
    'usage: python stripHTML.py inputCSV outputCSV columns\n' + \
    'example: python stripHTML.py messy_html.csv stripped.csv 4 5\n'
    exit()
    
if max(column) > len(next(csv.reader(open(csvFile)))):
    print '\nERROR: column does not exist \n' + \
    'usage: python stripHTML.py inputCSV outputCSV columns\n' + \
    'example: python stripHTML.py messy_html.csv stripped.csv 4 5\n'
    exit()
    
def process_the_html(csvFile,column):
	"""
	returns stripped column given csv and column number (not 0 indexed)
	"""
	csh = csv.reader(open(csvFile))
	next(csh,None)
	tmp = []
	for row in csh:
		tmp.append(row[column-1])
	newCol = [' '.join(re.findall('>(.+?)<',x)) for x in tmp]	# a list comprehension using regex to pull everything between tags -- might want to replace this with the HTML parser you use but I didn't have it 
	return newCol


#---------- Main Loop ----------#
c = 0 
for col in column:
	"""
	What I'm actually doing in this loop is creating a new temporary file 
	that I append the columns onto, then call the new file and make a new one 
	from that for every column given.  The last temporary file is then copied 
	to the "output" file as defined above and the extra temps are deleted.
	"""
	if c == 0: # I did some crazy/laxy flow control on this script.  If you want it to look pretty we can condense some of this
		tmpFile = open('XXXtmp.csv','w')
		fid = csv.reader(open(csvFile))
	if c > 0:
		try:
			tmpFile = open('XXXtmp%i.csv' % (c-1),'r')
		except IOError:
			tmpFile = open('XXXtmp.csv','r')
		fid = csv.reader(tmpFile)
		tmpFile = open('XXXtmp%i.csv' % c,'w')
	header = next(fid,None)
	for h in header:
		tmpFile.write('%s, ' % h)
	tmpFile.write('%s_stripped\n' % header[col-1])
	newCol = process_the_html(csvFile,col)
	for row,add in zip(fid,newCol):
		row.append(add)
		count = 1
		for r in row:
			if not count == len(row):
				tmpFile.write('%s, ' % r)
			else:
				tmpFile.write('%s\n' % r)
			count +=1
	tmpFile.close()
	c+=1

shutil.copyfile('XXXtmp%i.csv' % (c-1),output)
files = os.listdir('.')
for file in files:
    if file.startswith("XXXtmp"):
        os.remove(file)
	
