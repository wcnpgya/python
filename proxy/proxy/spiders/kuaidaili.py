# coding=utf8
from scrapy import Request, Spider
from proxy.db.db_helper import DB_helper
from proxy.detect.detect_proxy import Detect_Proxy
from proxy.detect.detect_manager import Detect_Manager
from proxy.items import ProxyItem
from scrapy.selector import Selector

'''
这个类的作用是将代理数据进行爬取
'''


class KuaiSpider(Spider):
    name = 'kuai'
    start_urls = [
                  "http://www.kuaidaili.com/free/inha/",
                  "http://www.kuaidaili.com/free/intr/",
                  "http://www.kuaidaili.com/free/outha/",
                  "http://www.kuaidaili.com/free/outtr/",
                ]
    allowed_domains = []
    db_helper = DB_helper()
    Page_Start = 1
    Page_End = 10
    detecter = Detect_Manager(5)
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en',
    }

    def parse(self, response):
        '''
        解析出其中的ip和端口
        :param response:
        :return:
        '''
        sel = Selector(response)
        item = ProxyItem()
        trs = sel.xpath('//tr')
        for tr in trs:
            tds = tr.xpath('./td/text()').extract()
        # ip = sel.xpath('//*[@id="index_free_list"]/table/tbody/tr/td[1]/text()').extract()
        # for i in range(10):
            for td in tds:
                content = td.strip()
                if len(content) > 0:
                    if content.isdigit():
                        item['port'] = content
                        break
                    if content.find('.') != -1:
                        item['ip'] = content
            yield item
        # if self.Page_Start < self.Page_End:
        # new_url = self.start_urls[0] + "proxylist" + str(range(self.Page_End) + 1)
            # self.Page_Start += 1
            # yield Request(new_url, headers=self.headers, callback=self.parse)
        for j in self.start_urls:
            for i in range(self.Page_End):
                new_url = j + str(i + 1)
                yield Request(new_url, headers=self.headers, callback=self.parse)

        yield Request("http://www.kuaidaili.com/proxylist/", headers=self.headers, callback=self.parse_item)

    def parse_item(self, response):
        sel = Selector(response)
        item = ProxyItem()
        ip = sel.xpath('//*[@id="index_free_list"]/table/tbody/tr/td[1]/text()').extract()
        port = sel.xpath('//*[@id="index_free_list"]/table/tbody/tr/td[2]/text()').extract()
        for i in range(10):
            item['ip'] = ip[i]
            item['port'] = port[i]
            yield item