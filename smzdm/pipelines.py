# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
from scrapy.conf import settings
from twisted.enterprise import adbapi
from scrapy.exceptions import DropItem

class SmzdmPipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb',db='scrapydb',user='root',passwd='root',charset='utf8',use_unicode=False)

    def process_item(self, item,spider):
        if item.get('web'):
            query = self.dbpool.runInteraction(self._conditional_insert,item)
            return item
        else:
            raise DropItem("Missing web, it's not a good!")

    def _conditional_insert(self,tx, item):
        if item.get('title'):
            tx.execute('insert into smzdm_data (picture,title,web,worthy,unworthy,price,web_url,good_describe) values (%s,%s,%s,%s,%s,%s,%s,%s)',(item['picture'],item['title'],item['web'],item['worthy'],item['unworthy'],item['price'],item['web_url'],item['describe']))
