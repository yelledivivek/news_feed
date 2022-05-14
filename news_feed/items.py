# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsFeedItem(scrapy.Item):
    # define the fields for your item here like:
    heading = scrapy.Field()
    description = scrapy.Field()
    story = scrapy.Field()
    image_urls = scrapy.Field()
