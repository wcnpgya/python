# coding=utf8
import argparse
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from proxy.spiders.xicidaili import XiciSpider




'''
cl
'''
if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Spider proxy -- ')
    parser.add_argument("-c", "-crawl", nargs="+", help="crawl proxy infor. example : python main.py -c 100 200",
                        type=int)
    parser.add_argument("-t", "-test", help="check proxy infor. command : python main.y -t db",
                   )
    args = parser.parse_args()

    if args.c is not None and len(args.c) > 1:
        #这个时候启动 爬虫
        print 'spider beginning ......'

        XiciSpider.Page_Start = args.c[0]
        XiciSpider.Page_End = args.c[1]
        process = CrawlerProcess(get_project_settings())
        process.crawl(XiciSpider)
        process.start()

        print 'spider end '
    elif args.t is not None:
        print 'detect begin ...... '
        XiciSpider.detecter.start()
        print 'detect end  '