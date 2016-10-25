import scrapy
import re
from smzdm.items import SmzdmItem

class smzdmSpider(scrapy.Spider):
    name  = "smzdm"
    start_urls = ['http://www.smzdm.com/jingxuan/',]

    def parse(self, response):
        sites = response.xpath('//li[@class="feed-row-wide"]')
        for site in sites:
            item = SmzdmItem()
            item['title'] = site.xpath('h5/a/@onclick').extract()
            item['price'] = site.xpath('h5/a/span/text()').extract()
            item['picture'] = site.xpath('div/div[@class="z-feed-img"]/a[@target="_blank"]/@href').extract()
            item['describe'] = site.xpath('div/div[2]/div[2]/strong/text()').extract()
            item['worthy'] = site.xpath('div/div[2]/div[3]/div[1]/span/a[1]/span[1]/span/text()').extract()
            item['unworthy'] = site.xpath('div/div[2]/div[3]/div[1]/span/a[2]/span[1]/span/text()').extract()
            item['web'] = site.xpath('div/div[2]/div[3]/div[2]/span/a/text()').extract()
            item['web_url'] = site.xpath('div/div[2]/div[3]/div[2]/div/div/a/@href').extract()
            yield item

        '''
        with open('smzdm.txt','w') as f:
            f.write(response.body)
        '''
        next_page = response.xpath('//a[@class="page-turn"]/@href').extract()[-1]
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
