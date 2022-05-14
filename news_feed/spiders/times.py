import scrapy
from scrapy.selector import Selector
from scrapy import item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from datetime import datetime, timedelta
from dateutil.parser import parse
from ..items import NewsFeedItem


class MySpider(CrawlSpider):
    name = 'times'
    allowed_domains = ['news18.com']
    start_urls = ['https://www.news18.com/']

    rules = (
        Rule(LinkExtractor(allow=('news/')),
             callback='parse_urls', follow=False),
    )

    def parse_urls(self, response):
        exists = response.css('div.story-container').extract()
        if exists:
            items = NewsFeedItem()
            heading = response.css('h1.article_heading::text').extract()
            description = response.css(
                'div.article_bnow_box > h2::text').extract()
            story = response.css(
                'article.article-content-box > div > p *::text').extract()
            st_image = response.css(
                'div.article_bimg > figure > div > img ::attr(src)').extract()
            clean_image_urls = []
            for img_url in st_image:
                clean_image_urls.append(response.urljoin(img_url))
            items['heading'] = heading
            items['description'] = description
            items['story'] = story
            items['image_urls'] = clean_image_urls
            yield items
        else:
            print(response.url)
        # items = NewsFeedItem()
        # global ti

        # time = response.css('ul.article_bnow li:nth-child(2)::text').extract()
        # for ti in time:
        #     ti = parse(ti.replace(' IST', ''))
        #     if (datetime.now() - ti) < timedelta(hours=1):
        #         heading = response.css('h1.article_heading::text').extract()
        #         items['heading'] = heading

        #         yield items
        #     else:
        #         print(response.url)
