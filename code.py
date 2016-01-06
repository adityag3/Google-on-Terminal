# This script is written by : Aditya Govil
# Github username : adityag3
# Website : http://adityagovil.co

#This module will help to extract useful data from a raw string
import re  
#This module will help to extract data from html code of the website
from bs4 import BeautifulSoup as BS  
#This module will bring all the html data from a website
import requests 
#This module will be used to access default browser ( google chrome )
import webbrowser

#It keeps collection of all the links of the search in it
links = []

#Base url of google.com which will provide static page for bs module to work
url = "http://google.com/search?q="

search = str(raw_input("Enter your search request: "))

print "Googling........."

html = requests.get(url + search)
html.raise_for_status()

soup = BS(html.text)

#Selects all the 'a' tags which are inside a tag with class = 'r'
# <tag class = 'r'><a href = '.....' >....</a></tag>
#               ^  ---------------------------
#                              ^
#                         Selected tag

tags = soup.select('.r a')

for tag in tags:
	raw_link = tag.get('href')
	raw_link = str(raw_link)
	links.append(raw_link)

#To make sure that no empty links are added to the list of links 'links'
if len(links) > 0:
	print "\n\nHELPFULL LINKS FOR YOUR SEARCH ARE: \n\n"
	print "--------------------------------------------\n"

	for link in links:
		print str(link)

	# Just to make things clear when displayed on terminal
	print "--------------------------------------------\n"


	choice =  raw_input("\n\n Would you like to see the answers on your browser(Y/N)? ")

	if choice == 'Y' or choice == 'y':
		count = 0

		# Only top 3 results will be displayed due to count variable
		for link in links:
			count = count + 1

			if count < 4:
				webbrowser.open('http://google.com' + str(link))
				#               --------------------------------
				#                             ^
				#           This link will be displayed on the browser

# When no link is found for the search request
else:
	print "=====TERMINANTED=====\n"
	print "NO RESULT FOUND FOR YOUR REQUEST!"



		