# -*- coding: utf-8 -*-
from scrapy.selector import Selector
import scrapy
from scrapy.http import Request
from scrapy.contrib.loader import ItemLoader, Identity
from meizi_scrapy.items import MeiziScrapyItem
class SexySpider(scrapy.Spider):
    name = "sexy"
    allowed_domains = ["mmjpg.com"]
    start_urls = ['http://www.mmjpg.com/']

    def parse(self, response):
        sel = Selector(response)
        urls = []

        urls = sel.xpath('/html/body/div[2]/div[1]/ul/li[1]/a/@href').extract()
        for url in urls:

        #url = 'http://www.mmjpg.com/home/3'
            yield Request(url, self.test)

    def test(self, response):
        pass
