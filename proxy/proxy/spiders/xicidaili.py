# coding=utf8
from scrapy import Request, Spider
from proxy.db.db_helper import DB_helper
from proxy.detect.detect_proxy import Detect_Proxy
from proxy.detect.detect_manager import Detect_Manager
from proxy.items import ProxyItem


'''
这个类的作用是将代理数据进行爬取
'''


class XiciSpider(Spider):
    name = 'xici'
    start_urls = ["http://www.xicidaili.com/nn/",
                  "http://www.xicidaili.com/wt/",
                  "http://www.xicidaili.com/wn/",
                  "http://www.xicidaili.com/nt/"]
    allowed_domains = []
    db_helper = DB_helper()
    detecter = Detect_Manager(5)
    Page_Start = 1
    Page_End = 5
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en',
        'Referer': 'http://www.xicidaili.com/'
    }

    def parse(self, response):
        '''
        解析出其中的ip和端口
        :param response:
        :return:
        '''

        trs = response.xpath('//tr[@class="odd" or @class=""]')
        for tr in trs:
            item = ProxyItem()
            tds = tr.xpath('./td/text()').extract()
            for td in tds:
                content = td.strip()
                if len(content) > 0:
                    if content.isdigit():
                        item['port'] = content
                        print 'ip:', item['ip']
                        print 'port:', item['port']
                        break
                    if content.find('.') != -1:
                        item['ip'] = content
            yield item
        for i in self.start_urls:
            for j in range(self.Page_End):
                new_url = i + str(j + 1)
                yield Request(new_url, headers=self.headers, callback=self.parse)