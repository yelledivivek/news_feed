import scrapy
from bs4 import BeautifulSoup
import requests
from ..items import NewsFeedItem


class IndianNews(scrapy.Spider):
    name = 'indian'

    html_text = requests.get('https://www.news18.com/').text
    soup = BeautifulSoup(html_text, 'lxml')
    news = soup.find_all('li', class_='fnt_siz_e')
    links = []
    for a in news:
        links.append(a.find('a', href=True)['href'])
    # str = 'https://www.indiatoday.in'
    # links = [str + x for x in links]

    start_urls = links

    def parse(self, response):
        items = NewsFeedItem()

        heading = response.css('h1.article_heading::text').extract()
        items['heading'] = heading

        yield items
