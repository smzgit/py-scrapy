import scrapy
from ..items import QuoteTutItem

class Quotes_spider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response, **kwargs):

        items = QuoteTutItem()

        quotes = response.css('.text::text').extract()
        aths = response.css('.author::text').extract()

        for q,a in zip(quotes,aths):
            items['quote'] = q
            items['author'] = a
            yield items

        next_pg = response.css('li.next a::attr(href)').get()

        if next_pg != None:
            yield response.follow(next_pg,callback=self.parse)