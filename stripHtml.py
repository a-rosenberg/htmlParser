# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 13:30:29 2016

@author: arosenbe
"""

# strip_the_html.py

### VARIABLES NEEDED FOR THE process_the_data function, which uses the strip_html function of MLStripper class
which_csv = "" # must be a csv, will be passed as a string
which_column = "" # not sure how to pass this (as a string) to correctly index the data, see note in process_the_html function below

# This defines the function, strip_tags to strip html markdown from text
from html.parser import HTMLParser

class MLStripper(HTMLParser):
	def __init__(self):
		self.reset()
		self.strict = False
		self.convert_charrefs= True
		self.fed = []
	def handle_data(self, d):
		self.fed.append(d)
	def get_data(self):
		return ''.join(self.fed)
        
def strip_html(html):
	s = MLStripper()
	s.feed(html)
	return s.get_data()
    
# This function, process_the_data, iterates strip_tags to read each row for the data col
def process_the_html(which_csv):
	# this takes a data frame
	import pandas as pd
	data = pd.read_csv(which_csv)
	
	temporary_list = []

	for i in data.index:
    	temporary_list = str(data['which_column -- GOES HERE, NOT SURE HOW TO INDEX THIS CORRECTLY'][i])
    	temporary_list = strip_html(temporary_list)
    	temporary_list = str.strip(temporary_list)
    	temporary_list.append(temporary_list)

	data['processed_column'] = temporary_list
	pd.DataFrame.to_csv(data, "which_csv") # this is minor, but maybe can we append "processed" to the end of this file name?

def main():