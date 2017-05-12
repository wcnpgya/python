# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging
from scrapy.exceptions import DropItem
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors
import json
import codecs


class JsonPipeline(object):
    def __init__(self):
        self.file = codecs.open('ebay2.json', 'w', encoding='utf8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()


class EbayPipeline(object):
        def __init__(self):
            self.dbpool = adbapi.ConnectionPool(
                dbapiName='MySQLdb',
                host='10.1.15.193',
                port=3306,
                db='python',
                user='mm',
                # passwd='VqoDFkSdiD8ICD5NklqdPqLQg',
                # passwd='d9U6ooizh7v6SrCYdr8iC5Wwh',
                passwd='123',
                cursorclass=MySQLdb.cursors.DictCursor,
                charset='utf8',
                use_unicode=False
            )
            self.urls_seen = set()

        def process_item(self, item, spider):
            # if item['url'] in self.urls_seen:
            #     raise DropItem("Duplicate items found: %s" % item)
            # else:
            query = self.dbpool.runInteraction(self._conditional_insert, item)
            query.addErrback(self._handle_error)
            return item

        def _conditional_insert(self, tx, item):
            # tx.executemany("select * from ebay WHERE brand_name = %s", ((item,) for item in item['brand_name']))
            # result = tx.fetchone()
            # if result:
            #     logging.log(logging.DEBUG, 'Item already stored in db:%s' % item,)
            # else:
            # tx.executemany("insert into ebay (brand_name) VALUES (%s)", ((item,) for item in item['brand_name']))
            # logging.log(logging.DEBUG, 'Item stored in db: %s' % item,)
            for each in item['brand_name']:
                tx.executemany("select * from ebay2 WHERE brand_name = %s", (each,))
                result = tx.fetchone()
                if result:
                    logging.log(logging.DEBUG, 'Item already stored in db:%s' % (each,))
                else:
                    tx.executemany("insert into ebay2 (brand_name) VALUES (%s)", (each,))
                    logging.log(logging.DEBUG, 'Item stored in db: %s' % (each,))

        def _handle_error(self, e):
            logging.warning(e)

