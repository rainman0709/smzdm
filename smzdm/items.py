# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item,Field


class SmzdmItem(Item):
    # define the fields for your item here like:
    # name = Field()
    title = Field()
    price = Field()
    address = Field()
    good_describe = Field()
    worthy = Field()
    unworthy = Field()
    web = Field()
    web_url = Field()
    image_urls = Field()
    images = Field()
    good_time = Field()
