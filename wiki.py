#!/usr/bin/env python3
import webbrowser
import sys
import requests
import re

# Opens a url in a new tab of the users browser
def open_url(url):

	webbrowser.open_new_tab(url) 

# Opens a random article in a specified language, default language is English 
def random_article(language):

	if(language == None): language = 'en'
	url = 'https://'+language+".wikipedia.org/wiki/Special:Random"
	open_url(url)

# Opens a random article in a specified category
# This function uses https://randomincategory.toolforge.org to find a random page in a given category
# Limitations: this tool searches English wikipedia, user cannot customize a language here

def category_article(category):

	article_name = None

# Non-article Wikipedia pages 
	unwanted_titles = (b"Category", b"Portal", b"User", b"Contents")

# Searches for the first page that is not in the unwanted_tiles list
	while(article_name == None):

		link = "https://randomincategory.toolforge.org/"+category+"?site=en.wikipedia.org"
		f = requests.get(link, stream=True)

		for line in f.iter_lines():
			if b'<title>' in line:
				if any(word in line for word in unwanted_titles):
					break;
				else:
					article_name = line
					break

# Regex to remove HTML and get pure article title 
	m = re.match(rb"^<title>([\w\s]*)",article_name)
	article_name = m.group(1).strip()

# Convert from 8-bit unicode to string 
	article_name = article_name.decode("utf-8")

# Replace spaces with underscore to transform into a new wikipedia url 
	article_name = article_name.replace(" ","_")

	url = 'https://en.wikipedia.org/wiki/'+article_name
	open_url(url)

#process language codes from language-codes.csv
import csv

languages = []

with open('language-codes.csv', 'rt') as f:
    reader = csv.reader(f,delimiter="\n")
    for row in reader:
    	 languages.append((row[0].split(',')[0]))

#default language is English
language = 'en'

#change default language if user enters arg
if len(sys.argv) - 1 == 0:
	random_article(language)

if len(sys.argv) - 1 > 0:
	if sys.argv[1] in languages: 
		language = sys.argv[1]
		if sys.argv[2]: category_article(sys.argv[2])
		else: random_article(language)
	else:
		category = sys.argv[1]
		category_article(category)


