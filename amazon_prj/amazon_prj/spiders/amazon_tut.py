import scrapy
from ..items import AmazonPrjItem

class AmazonTutSpider(scrapy.Spider):
    name = 'amazon_tut'
    pg_num=2
    start_urls = ['https://www.amazon.in/s?k=amazon+books+store&adgrpid=59956079195&ext_vrnc=hi&hvadid=295070573273&hvdev=c&hvlocphy=9062093&hvnetw=g&hvqmt=b&hvrand=16749890251705647179&hvtargid=kwd-294893494267&hydadcr=23636_1725033&qid=1653895375&ref=sr_pg_1']

    def parse(self, response):
        items = AmazonPrjItem()
        prod_name = response.css('.a-text-normal .a-text-normal::text').extract()
        prod_author = response.css('.a-color-secondary .a-size-base.s-link-centralized-style').css('::text').extract()
        prod_price = response.css('.s-price-instructions-style .a-price-whole').css('::text').extract()
        prod_img = response.css('.s-image').get()

        items['prod_name'] = prod_name
        items['prod_author'] = prod_author
        items['prod_price'] = prod_price
        items['prod_img'] = prod_img

        yield items

        nxt_pg = 'https://www.amazon.in/s?k=amazon+books+store&page='+str(AmazonTutSpider.pg_num)+'&adgrpid=59956079195&ext_vrnc=hi&hvadid=295070573273&hvdev=c&hvlocphy=9062093&hvnetw=g&hvqmt=b&hvrand=16749890251705647179&hvtargid=kwd-294893494267&hydadcr=23636_1725033&qid=1653895793&ref=sr_pg_2'
        if AmazonTutSpider.pg_num < 20:
            AmazonTutSpider.pg_num += 1
            yield response.follow(nxt_pg, callback=self.parse)

