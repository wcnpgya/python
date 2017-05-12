# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from scrapy.contrib.loader import ItemLoader, Identity
from meizi_scrapy.items import MeiziScrapyItem

class MeiziSpider(scrapy.Spider):
    name = "meizi"
    allowed_domains = ["mmjpg.com"]
    start_urls = ['http://www.mmjpg.com/home/2']

    # rules = (
    #     Rule(LinkExtractor(allow=('/home/2'), ),
    #          callback='parse_operate',
    #          ),
    # )

    def parse(self, response):
        sel = Selector(response)
        page_temp_data = sel.xpath('/html/body/div[2]/div[1]/div/a[9]/@href').extract()[0]
        us = page_temp_data.split('/')
        page = us.pop()
        for index in range(1, int(page)):
            url = 'http://www.mmjpg.com/home/' + str(index)
            yield Request(url, self.parse_second)

        # test
        links = []
        # url = 'http://www.mmjpg.com/home/3'
        # yield Request(url, self.parse_second)

        #bug  link can't get last page
        # links = sel.xpath('/html/body/div[2]/div[1]/div/em[2]/following-sibling::*[1]/@href').extract()
        # for link in links:
        #     if len(link):
        #         aimurl = 'http://www.mmjpg.com' + link
        #         # yield Request(aimurl, self.parse)
        #         yield Request(aimurl, self.parse_second)
        #     else:
        #         pass

    def parse_second(self, response):
        sel = Selector(response)
        links = sel.xpath('/html/body/div[2]/div[1]/ul/li/a/@href').extract()
        for link in links:

            yield Request(link, self.parse_final)

    def parse_final(self, response):
        # sel = Selector(response)
        # item = MeiziScrapyItem()
        # item["image_name"] = sel.xpath('/html/body/div[2]/div[1]/h2/text()').extract()[0]
        # return item
        l = ItemLoader(item=MeiziScrapyItem(), response=response)
        l.add_xpath('image_name', '/html/body/div[2]/div[1]/h2/text()')
        l.add_xpath('image_url', '//*[@id="content"]/a/img/@src')
        l.add_xpath('page_total_num', '//*[@id="page"]/a[7]/text()')
        return l.load_item()

