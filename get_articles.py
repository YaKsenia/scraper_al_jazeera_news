# Scrape articles' texts and titles using Python library Newspaper (from Al Jazeera website, but can be used for others as well)


import newspaper
from newspaper import Article
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Firefox()
#read the csv-file with links to articles
df = pd.read_csv('/home/ksenia_new/projects/scraping_thesis/al_jazeera_scripts/al_jazeera_links_new.csv', sep=',', low_memory=False, na_values = ['no info', '.'])
links = list(df['links'])
urls = []
headers = []
texts = []
for url in links:

		#create an Article object with the url
		article = Article(url)
		article.download()
		article.parse()
		#print(article.title)
		#print(article.text)
		urls.append(url)

		#append article title to the list
		headers.append(article.title)

		#append article text to the list
		texts.append(article.text)

		driver.implicitly_wait(5)


final = pd.DataFrame({ 'url' : urls, 'title' : headers, 'text' : texts})

final.to_csv('jazeera_articles_new.csv')