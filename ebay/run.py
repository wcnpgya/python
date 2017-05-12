# coding=utf8
from scrapy import log
from scrapy import signals
from scrapy.crawler import Crawler
from twisted.internet import reactor
from scrapy.utils.project import get_project_settings


class manage:

    spiderCounter = 0

    def setupCrawler(self, spiderName):
        crawler = Crawler(get_project_settings())
        crawler.signals.connect(self.spiderClosed, signal=signals.spider_closed)
        #crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
        crawler.configure()

        spider = crawler.spiders.create(spiderName)

        crawler.crawl(spider)
        crawler.start()


    def spiderClosed(self):
        self.spiderCounter -= 1

        if self.spiderCounter == 0:
            reactor.stop()


    def run(self):
        crawler = Crawler(get_project_settings())
        crawler.configure()
        log.start()
        for spiderName in crawler.spiders.list():
            self.spiderCounter += 1
            self.setupCrawler(spiderName)

        reactor.run()


if __name__ == '__main__':
   handle = manage()
   handle.run()
