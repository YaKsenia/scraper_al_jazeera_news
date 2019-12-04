# Scrape articles' texts and titles using Python library Newspaper (from Al Jazeera website, but can be used for others as well)

import newspaper
from newspaper import Article
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def get_articles(df):

	driver = webdriver.Firefox()
	urls = []
	headers = []
	texts = []
	for url in df['links']:

			#create an Article object with the url
			article = Article(url)
			article.download()
			article.parse()
			print(article.title)
			#print(article.text)
			urls.append(url)
			#append article title to the list
			headers.append(article.title)
			#append article text to the list
			texts.append(article.text)
			driver.implicitly_wait(5)


	df['title'] = headers
	df['text'] = texts

	return df