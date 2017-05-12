# coding=utf8
import os
from pymongo import MongoClient

class DB(object):
    def __init__(self):
        MONGODB_HOST = '10.1.15.193'
        MONGODB_PORT = 37017
        MONGODB_DBNAME = 'proxy'

        client = MongoClient(MONGODB_HOST, MONGODB_PORT)
        db = client[MONGODB_DBNAME]
        self.proxys = db.proxys

    def find(self):
        proxys = self.proxys.find()
        proxyID = 1
        for proxy in proxys:
            ip = proxy['ip']
            port = proxy['port']
            command = "casperjs --proxy=%s:%s" % (ip, port)
            proxyID += 1
            os.popen(command, )