# coding=utf8
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from ebay.items import EbayItem
import json
from scrapy.crawler import CrawlerProcess
import re


class EbaySpider(CrawlSpider):
    name = 'ebay'
    allowed_domains = ['ebay.com']
    start_urls = [
        'http://www.ebay.com/sch/sch/allcategories/all-categories',
    ]
    rules = (
        # Rule(LinkExtractor(allow=('http://www.ebay.com/chp/.*/\d*$'), restrict_xpaths=('//*[@class="gcma"]/ul[position()>4 and position()<8]/li/a')),
        #      # process_request='parse_operate',
        #      callback='parse_operate',
        #      ),
        # Rule(LinkExtractor(allow=('http://www.ebay.com/chp/.*/\d*$'), restrict_xpaths=('//*[@class="gcma"]/ul[position()>10 and position()<14]/li/a')),
        #      callback='parse_operate',
        #      ),
        # Rule(LinkExtractor(allow=('http://www.ebay.com/sch/.*/\d*/i.html$'), restrict_xpaths=('//*[@class="gcma"]/ul[position()>13 and position()<23]/li/a')),
        #      callback='parse_operate',
        #      ),
        # Rule(LinkExtractor(allow=('http://www.ebay.com/sch/.*/\d*/i.html$'), restrict_xpaths=('//*[@class="gcma"]/ul[position()>28 and position()<35]/li/a')),
        #      callback='parse_operate',
        #      ),
        # Rule(LinkExtractor(allow=('http://www.ebay.com/sch/.*/\d*/i.html$'), restrict_xpaths=('//*[@class="gcma"]/ul[position()>52 and position()<59]/li/a')),
        #      callback='parse_operate',
        #      ),
        # Rule(LinkExtractor(allow=('http://www.ebay.com/chp/.*/\d*$'), restrict_xpaths=('//*[@class="gcma"]/ul[position()>64 and position()<71]/li/a')),
        #      callback='parse_operate',
        #      ),
        # Rule(LinkExtractor(allow=('http://www.ebay.com/chp/.*/\d*$'), restrict_xpaths=('//*[@class="gcma"]/ul[position()>80 and position()<84]/li/a')),
        #      callback='parse_operate',
        #      ),
        # Rule(LinkExtractor(allow=('http://www.ebay.com/sch/.*/\d*/i.html$'), restrict_xpaths=('//*[@class="gcma"]/ul[position()>89 and position()<93]/li/a')),
        #      callback='parse_operate',
        #      ),
        # Rule(LinkExtractor(allow=('http://www.ebay.com/sch/.*/\d*/i.html$'), restrict_xpaths=('//*[@class="gcma"]/ul[59]/li[4]/a')),
        #      callback='parse_operate',
        #      ),
        # Rule(LinkExtractor(allow=('http://www.ebay.com/sch/.*/\d*/i.html$'), restrict_xpaths=('//*[@class="gcma"]/ul[61]/li[3]/a')),
        #      callback='parse_operate',
        #      ),
        # Rule(LinkExtractor(allow=('http://www.ebay.com/sch/.*/\d*/i.html$'), restrict_xpaths=('//*[@class="gcma"]/ul[61]/li[1]/a')),
        #      callback='parse_operate',
        #      ),
        # Rule(LinkExtractor(allow=('http://www.ebay.com/chp/.*/\d*$'), restrict_xpaths=('//*[@class="gcma"]/ul[64]/li[1]/a')),
        #      callback='parse_operate',
        #      ),
        # Rule(LinkExtractor(allow=('http://www.ebay.com/sch/.*/\d*/i.html$'), restrict_xpaths=('//*[@class="gcma"]/ul[96]/li[3]/a')),
        #      callback='parse_operate',
        #      ),
        Rule(LinkExtractor(allow=('http://www.ebay.com/chp/.*/\d*$'),),
             callback='parse_operate',
             ),
        Rule(LinkExtractor(allow=('http://www.ebay.com/sch/.*/\d*/i.html$'),),
             callback='parse_operate',
             ),

    )

    def parse_operate(self, response):
        url = response.url
        us = url.split('/')
        temp = list(us[4])
        temp.pop()
        result = ''.join(temp)
        us[4] = result
        rurl = '/'.join(us)
        aim_url = rurl + '?_ssan=Brand'
        yield Request(aim_url, callback=self.parse_result)

    def parse_result(self, response):
        item = EbayItem()
        jsDict = json.loads(response.body)
        if len(jsDict):
            jsvalues = jsDict.get('values', 'this page has no brand message')
            result = []
            item['url'] = response.url
            for each in jsvalues:
                # item['brand_name'] = [each['title']]
                # yield item

                result.append(each['title'])
            item['brand_name'] = result
            return item
        else:
            print 'Useless url!!!'

# process = CrawlerProcess()
# process.crawl(EbaySpider)
# process.start()