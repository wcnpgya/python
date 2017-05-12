# coding=utf8
from threading import Thread
import time
from proxy.db.db_helper import DB_helper
from proxy.detect.detect_proxy import Detect_Proxy

'''
    definition a thread
    '''
class Detect_Manager(Thread):

    def __init__(self, threadeSum):
        Thread.__init__(self)
        sqldb = DB_helper()#恢复序号
        sqldb.updateID()
        self.pool = []
        for i in range(threadeSum):
            self.pool.append(Detect_Proxy(DB_helper(), i + 1, threadeSum))

    def run(self):
        self.startManager()
        self.checkState()

    def startManager(self):
        for thread in self.pool:
            thread.start()

    def checkState(self):
        '''
        检测线程状态
        :return:
        '''
        now = 0
        while now < len(self.pool):
            for thread in self.pool:
                if thread.isAlive():
                    now = 0
                    break
                else:
                    now += 1
            time.sleep(1)
        goodNum = 0
        badNum = 0
        for i in self.pool:
            goodNum += i.goodNum
            badNum += i.badNum

        sqldb = DB_helper()
        sqldb.updateID()
        print 'good NUM ---', goodNum
        print 'bad NUM ---', badNum

