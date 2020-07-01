#!/usr/bin/env python3
import webbrowser
import sys
import requests
import re

def open_url(url):

	webbrowser.open_new_tab(url) 

def random_article(language):

	if(language == None): language = 'en'
	url = 'https://'+language+".wikipedia.org/wiki/Special:Random"
	open_url(url)

def category_article(category):
	article_name = None
	unwanted_titles = (b"Category", b"Portal", b"User", b"Contents")

	while(article_name == None):

		link = "https://randomincategory.toolforge.org/"+category+"?site=en.wikipedia.org"
		f = requests.get(link, stream=True)

		for line in f.iter_lines():
			if b'<title>' in line:

				if any(word in line for word in unwanted_titles):
					break;
				else:
					print(line)
					article_name = line
					break

	m = re.match(rb"^<title>([\w\s]*)",article_name)
	article_name = m.group(1).strip()

	article_name = article_name.decode("utf-8")
	article_name = article_name.replace(" ","_")

	url = 'https://en.wikipedia.org/wiki/'+article_name
	open_url(url)

languages = {
	
	"en" : "English",
	"es" : "Spanish",
	"run" : "Russian",
	"pl" : "Polish",
	"simple" : "Simple English Wikipedia"
}

usage = "Usage: wiki.py [language] [search_term]"

#default language is English
language = 'en'

#change default language if user enters arg
if len(sys.argv) - 1 == 0:
	random_article(language)

if len(sys.argv) - 1 > 0:
	if sys.argv[1] in languages: 
		language = sys.argv[1]
		random_article(language)
	else:
		category = sys.argv[1]
		category_article(category)

