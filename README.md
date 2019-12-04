# Scraper of news articles from Al Jazeera/ AJ/ Аль-Джазира website (https://www.aljazeera.com/)

Python scripts which scrape links of news from Al Jazeera search and then scrape news texts and headers from these links

(Описание на русском ниже)

This project collects news articles' titles and texts from the website of Al Jazeera news agency. You can choose any topic, from which you want to get the articles. Unfortuntely Al Jazeera website does not allow to choose particular dates in the search engine, so you have to look manually at which page of search results the period which you are interested in, starts. For example, in our case the start page was 81, the end page - 91. If you want to get all the articles on some topic, you can specify 1 as a start page and the last page of results as an end page.


Before running the project, you have to install the necessary software typing this command in your Terminal/command line:

**python3.6 -m pip install -r requirements.txt --upgrade**

Then you should go to https://www.aljazeera.com/, choose the keywords  you are interested in, copy the resulting link and replace the link in settings.py file with this url.

![alt text](https://github.com/YaKsenia/scraper_al_jazeera_news/blob/master/output/copy_link.png)

In settings.py file you also need to specify the start and end pages of the period you would like to scrape. **It is important to specify correct numbers, otherwise the program will not be able to scrape the page which doesn't exist (e.g. if you choose 92 as an end page and there are only 90 pages in your search results, it will not work)**

then you can just run the file main_aj.py using this command in your Terminal:

**python3.6 main_aj.py**

Your browser window will be opened automatically. You don't have to do anything, just wait and don't close the window (you can do whatever you want in other programs while this one will be executed). This is what you will see:


![alt text](https://github.com/YaKsenia/scraper_al_jazeera_news/blob/master/output/browser.png)

![alt text](https://github.com/YaKsenia/scraper_al_jazeera_news/blob/master/output/output1.png)

![alt text](https://github.com/YaKsenia/scraper_al_jazeera_news/blob/master/output/output2.png)


After the browser will be closed, the program will continue executing in the Terminal and you will see headlines of scraped articles:

![alt text](https://github.com/YaKsenia/scraper_al_jazeera_news/blob/master/output/output3.png)


The resulting csv-file will be saved in the folder of the project (you can see example in the folder "output" now). No matter how many articles will be in your results, the script automatically scrolls the webpage down until it reaches the end and scrapes all the articles.

This is how resulting file looks like:

![alt text](https://github.com/YaKsenia/scraper_al_jazeera_news/blob/master/output/resulting_file.png)








*Translation to Russian/ Перевод на русский:*



Эта программа скачивает заголовки и тексты новостных статей с сайта российского новостного  агентства Al Jazeera/ AJ/ Аль-Джазира. Вы можете выбрать любые ключевые слова, по которым вы хотите получить статьи.

Перед запуском проекта вам необходимо установить необходимое программное обеспечение, набрав эту команду в вашем терминале (командной строке):

**python3.6 -m pip install -r requirements.txt --upgrade**


Затем вам нужно перейти на https://www.aljazeera.com/, выбрать ключевые слова, которые вас интересуют, скопировать получившуюся ссылку и заменить ссылку в файле settings.py этим URL. К сожалению, сайт Al Jazeera не позволяет выбирать конкретные даты в поисковой системе, поэтому вам нужно вручную посмотреть, с какой страницы результатов поиска начинается интересующий вас период. Например, в нашем случае начальная страница была 81, конечная страница - 91. Если вы хотите получить все статьи по какой-либо теме, вы можете указать 1 в качестве начальной страницы и последнюю страницу результатов в качестве конечной страницы.

В файле settings.py вам также нужно указать начальную и конечную страницы периода, за который вы хотите получить статьи. ** Важно указать правильные номера страниц, иначе программа не сможет найти несуществующую страницу (например, если вы выберете 92 в качестве конечной страницы и в результатах поиска будет только 90 страниц, она не будет работать)**


![alt text](https://github.com/YaKsenia/scraper_al_jazeera_news/blob/master/output/copy_link.png)

Теперь вы можете просто запустить файл main_aj.py с помощью этой команды в вашем терминале\командной строке:


**python3.6 main_aj.py**


Окно вашего браузера будет открыто автоматически. Вам не нужно ничего делать, просто ждите и не закрывайте окно (вы можете делать все, что захотите, в других программах, пока эта будет выполняться). Вот что вы должны увидеть:


![alt text](https://github.com/YaKsenia/scraper_al_jazeera_news/blob/master/output/scraping_browser.png)

![alt text](https://github.com/YaKsenia/scraper_al_jazeera_news/blob/master/output/output1.png)

![alt text](https://github.com/YaKsenia/scraper_al_jazeera_news/blob/master/output/output2.png)


После того, как браузер закроется, программа продолжит работу в Терминале\командной строке, и вы увидите заголовки загруженных статей:


![alt text](https://github.com/YaKsenia/scraper_al_jazeera_news/blob/master/output/output3.png)

Результаты загрузки будут сохранены в CSV-файле в папке проекта (вы можете увидеть пример в папке «output»). 


![alt text](https://github.com/YaKsenia/scraper_al_jazeera_news/blob/master/output/resulting_file.png)
