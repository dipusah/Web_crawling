#BeautifulSoup Documentation
#Web Crawling- To extract data from various websites.
import requests
#import os
from bs4 import BeautifulSoup

BASE_URL='https://www.onlinekhabar.com'

home_page = requests.get(BASE_URL)
print(home_page.content) #'content' prints all the HTML tags in the website... text prints the HTML & CSS

home_page_content = BeautifulSoup(home_page.content,'html.parser')

links=set()                                   #For removing repetition(Unique link)

for a_tag in home_page_content.find_all('a'): #'a' tag links two pages. (Hyperlink inside)
    print(a_tag['href'])                      # link is inside 'href'
    if'/2018/' in a_tag['href']:
        links.add(a_tag['href'])

with open('onlinekhabar-news.txt','w',encoding='utf-8') as news_file:  #UTF-UNICODE
     for link in links:
         single_page_news = requests.get(link)
         single_page_content = BeautifulSoup(single_page_news.content,'html.parser')
         real_content = single_page_content.select_one('.ok-single-content') #find(select_one), .gives the class
         print(real_content.text)
         news_file.write(str(real_content))
         news_file.write('\n')
