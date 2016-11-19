import scrapy
import re
from smzdm.items import SmzdmItem
import hashlib

class smzdmSpider(scrapy.Spider):
    name  = "smzdm"
    start_urls = ['http://www.smzdm.com/jingxuan/',]

    def parse(self, response):
        sites = response.xpath('//li[@class="feed-row-wide"]')
        for site in sites:
            item = SmzdmItem()
            title = site.xpath('h5/a/text()').extract()
            item['title'] = title[0].strip().encode('utf-8') if len(title) > 0 else ''

            price = site.xpath('h5/a/span/text()').extract()
            item['price'] = price[0].encode('utf-8') if len(price) > 0 else ''

            address = site.xpath('div/div[@class="z-feed-img"]/a[@target="_blank"]/@href').extract()
            item['address'] = address[0].encode('utf-8') if len(address) > 0 else ''

            item['image_urls'] = site.xpath('div/div[@class="z-feed-img"]/a[@target="_blank"]/img/@src').extract()
            good_describe = site.xpath('div/div[2]/div[2]/strong/text()').extract()
            item['good_describe'] = good_describe[0].encode('utf-8') if len(good_describe) > 0 else ''

            worthy = site.xpath('div/div[2]/div[3]/div[1]/span/a[1]/span[1]/span/text()').extract()
            item['worthy'] = worthy[0].encode('utf-8') if len(worthy) > 0 else ''

            unworthy = site.xpath('div/div[2]/div[3]/div[1]/span/a[2]/span[1]/span/text()').extract()
            item['unworthy'] = unworthy[0].encode('utf-8') if len(unworthy) > 0 else ''

            web = site.xpath('div/div[2]/div[3]/div[2]/span/a/text()').extract()
            item['web'] = web[0].encode('utf-8') if len(web) > 0 else ''

            web_url = site.xpath('div/div[2]/div[3]/div[2]/div/div/a/@href').extract()
            item['web_url'] = web_url[0].encode('utf-8') if len(web_url) > 0 else ''

            images = site.xpath('div/div[@class="z-feed-img"]/a[@target="_blank"]/img/@src').extract()
            item['images'] = hashlib.sha1(images[0].encode('utf-8') if len(images) > 0 else '').hexdigest()

            good_time = site.xpath('div/div[2]/div[3]/div[2]/span/text()').extract()
            item['good_time'] = good_time[0].strip().encode('utf-8') if len(web_url) > 0 else ''
            yield item

        '''
        with open('smzdm.txt','w') as f:
            f.write(response.body)
        '''
        next_page = response.xpath('//a[@class="page-turn"]/@href').extract()[-1]
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
