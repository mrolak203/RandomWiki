#!/usr/bin/env python3
import webbrowser
import sys

languages = {
	
	"en" : "English",
	"es" : "Spanish",
	"run" : "Russian",
	"pl" : "Polish",
	"simple" : "Simple English Wikipedia"
}

#default language is English

usage = "Usage: ./wiki [language]"

language = 'en'

if len(sys.argv) - 1 > 0:
	language = sys.argv[1]


webbrowser.open_new_tab('https://'+language+".wikipedia.org/wiki/Special:Random") 


#https://en.wikipedia.org/wiki/Special:RandomInCategory