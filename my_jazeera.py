#this script scrapes all the links of the news articles from the website of Al Jazeera (search)

#How to use it?

#Go to https://www.aljazeera.com/Search/ and choose the keywords you want to search for

#Copy the link with your keywords (e.g. we were looking for "Russia syria war" and the link was this:
#'https://www.aljazeera.com/Search/?q=russia%20syria%20war')

#If you want to scrape the news of a particular time period, unfortunately Al Jazeera doesn't
#have filter by date. So what we do - manually check the numbers of pages with the dates 
#we want to scrape and use them in the "for" loop (e. g. we needed only articles from pages 
#81 - 91. The scraper clicks on the pages from the first one until it gets the page numbers
#which you want and starts scraping only them)


from bs4 import BeautifulSoup, SoupStrainer
import urllib.request as urllib2
import re
import requests
import pandas as pd
from headers import HEADERS
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


driver = webdriver.Firefox()
#open the link
driver.get('https://www.aljazeera.com/Search/?q=russia%20syria%20war')
driver.maximize_window()

#close the banner on the website
driver.find_element_by_id('ensCloseBanner').click()


try:
	#this is a page number, it will be updated after every time the scraper clicks on a page
	number = 1
	links = []
	for i in range (0, 91):

			#find the button with page number and click

			driver.find_element_by_link_text(str(number)).click()
			print ('clicked page',  number)

			#wait 10 sec so the website will not think we are robots
			driver.implicitly_wait(10)

			#here you should specify the range of pages you want to scrape (you can start with 1)
			if number >= 81 and number <= 91:
				html = driver.page_source
				html = BeautifulSoup(html, "lxml")
				articles = html.find_all('div', {'class': 'col-sm-7 topics-sec-item-cont'})

				for article in articles:

					#find all links on the page
					ankor_list = article.findChildren('a')

					for ankor in ankor_list:

					    url = ankor.get('href')
					    url = 'https://www.aljazeera.com' + url
					    #save url only if it is a news or opinion article (so we get read of social media links, advertisements etc.)
					    if 'news' in url or 'opinion' in url:
						    links.append(url)


				#go to the next page
				number = number + 1
			#print(links)

			#to speed up the process, before we achieve the number of page that we want to start with, 
			#click on every 4th page instead of every 1st
			
			elif number < 81:
				number = number + 4

			else:
				
				#break after we scrape the last page
				break

	#print(links)
	
	#save the links as Pandas dataframe, drop duplicates and save as a csv-file
	links = pd.DataFrame({'links' : links })
	links = links.drop_duplicates(subset='links', keep='last', inplace=False)
	links.to_csv('al_jazeera_links_check.csv')

except Exception as e:
	print(e)

finally:
	driver.quit()
	print('Finished.')
