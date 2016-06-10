# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 13:30:29 2016

@author: arosenbe
"""
#from html.parser import HTMLParser
import sys
import re
import csv

#if not len(sys.argv) == 3:
#	print 'ERROR: incorrect number of inputs\n' + \
#		'usage: python stripHtml.py csvPath column'
		

# strip_the_html.py

### VARIABLES NEEDED FOR THE process_the_data function, which uses the strip_html function of MLStripper class
csvFile = 'messy_html.csv' # must be a csv, will be passed as a string
column = [4] # not sure how to pass this (as a string) to correctly index the data, see note in process_the_html function below

# This defines the function, strip_tags to strip html markdown from text
#
#class MLStripper(HTMLParser):
#	def __init__(self):
#		self.reset()
#		self.strict = False
#		self.convert_charrefs= True
#		self.fed = []
#	def handle_data(self, d):
#		self.fed.append(d)
#	def get_data(self):
#		return ''.join(self.fed)
#        
#def strip_html(html):
#	s = MLStripper()
#	s.feed(html)
#	return s.get_data()
    
# This function, process_the_data, iterates strip_tags to read each row for the data col
def process_the_html(csvFile,column):
	for col in column:
		print col
		csh = csv.reader(open(csvFile))
		header = next(csh,None)
		tmp = []
		for row in csh:
			print row
			tmp.append(row[col-1])
		newCol = [re.findall('>(.+?)<',x)[0] for x in tmp]	
	return newCol
	
	
	
	
	
	
	
	
	
	
#	
#	
#	
#	
#	# this takes a data frame
#	data = pd.read_csv(column)
#	
#	temporary_list = []
#
#	for i in data.index:
#    	temporary_list = str(data['which_column -- GOES HERE, NOT SURE HOW TO INDEX THIS CORRECTLY'][i])
#    	temporary_list = strip_html(temporary_list)
#    	temporary_list = str.strip(temporary_list)
#    	temporary_list.append(temporary_list)
#
#	data['processed_column'] = temporary_list
#	pd.DataFrame.to_csv(data, "which_csv") # this is minor, but maybe can we append "processed" to the end of this file name?

newCol = process_the_html(csvFile,column)