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
    picture = Field()
    describe = Field()
    worthy = Field()
    unworthy = Field()
    web = Field()
    web_url = Field()
