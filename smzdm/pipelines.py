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
        update = tx.execute("select 1 from scrapydb.smzdm_back where address = '{0}'".format(item['address']))
        if update:
            tx.execute("update scrapydb.smzdm_back set address = '{0}',title = '{1}',web = '{2}',worthy = '{3}',unworthy = '{4}',price = '{5}',web_url = '{6}',good_describe = '{7}',images = '{8}',good_time = '{9}' where address = '{10}'".format(item['address'],MySQLdb.escape_string(item['title']),MySQLdb.escape_string(item['web']),item['worthy'],item['unworthy'],MySQLdb.escape_string(item['price']),item['web_url'],MySQLdb.escape_string(item['good_describe']),item['images'],item['good_time'],item['address']))
        else:
            tx.execute("insert into scrapydb.smzdm_back (address,title,web,worthy,unworthy,price,web_url,good_describe,good_time) values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}')".format(item['address'],MySQLdb.escape_string(item['title']),MySQLdb.escape_string(item['web']),item['worthy'],item['unworthy'],MySQLdb.escape_string(item['price']),item['web_url'],MySQLdb.escape_string(item['good_describe']),item['good_time']))
