from scrape_links import get_links
from scrape_articles import get_articles
from settings import *

links_df = get_links(url, start_page, end_page)

articles = get_articles(links_df)

articles.to_csv('Scraped_Al_Jazeera_articles.csv')