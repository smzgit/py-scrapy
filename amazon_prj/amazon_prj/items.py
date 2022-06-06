# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonPrjItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    prod_name = scrapy.Field()
    prod_author = scrapy.Field()
    prod_price = scrapy.Field()
    prod_img = scrapy.Field()
