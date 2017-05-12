# coding=utf8
import socket
from threading import Thread

import urllib

'''
test ip
'''
class Detect_Proxy(Thread):

    url = 'http://ip.chinaz.com/getip.aspx'

    def __init__(self, db_helper, part, sum):
        Thread.__init__(self)
        self.db_helper = db_helper
        self.part = part #检测的分区
        self.sum = sum #检测的总区域

        self.counts = self.db_helper.proxys.count()
        socket.setdefaulttimeout(2)
        self.__goodNum = 0
        self.__badNum = 0

    @property
    def goodNum(self):
        return self.__goodNum

    @goodNum.setter
    def goodNum(self, value):
        self.goodNum = value

    @property
    def badNum(self):
        return self.__badNum

    @badNum.setter
    def badNum(self, value):
        self.badNum = value

    def run(self):
        self.detect() #begin to test

    def detect(self):
        '''
        http://ip.chinaz.com/getip.aspx is the aim net to test
        :return:
        '''
        if self.counts < self.sum: #if count num less than all num error
            return

        pre = self.counts / self.sum
        start = pre * (self.part-1)
        end = pre * self.part
        if self.part == self.sum:#如果是最后一部分，结束就是末尾
            end = self.counts
        # print 'pre-%d-start-%d-end-%d'%(pre,start,end)

        proxys = self.db_helper.proxys.find({'proxyId': {'$gt': start, '$lte': end}})#大于start小于等于end,很重要

        for proxy in proxys:

            ip = proxy['ip']
            port = proxy['port']
            try:
                proxy_host ="http://ha:ha@" + ip +':'+port #为了防止填写账户名密码暂停的情况
                response = urllib.urlopen(self.url, proxies={"http": proxy_host})
                if response.getcode() != 200:
                    self.db_helper.delete({'ip': ip, 'port': port})
                    self.__badNum += 1
                    print proxy_host, 'bad proxy'
                else:
                    self.__goodNum += 1
                    print proxy_host, 'success proxy'

            except Exception, e:

                print 'bad proxy'
                self.db_helper.delete({'ip': ip, 'port': port})
                self.__badNum += 1
                continue


