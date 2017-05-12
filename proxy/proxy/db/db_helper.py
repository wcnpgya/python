# coding=utf8
from pymongo import MongoClient


class DB_helper(object):
    def __init__(self):
        MONGODB_HOST = '10.1.15.193'
        MONGODB_PORT = 37017
        MONGODB_DBNAME = 'proxy'

        client = MongoClient(MONGODB_HOST, MONGODB_PORT)
        db = client[MONGODB_DBNAME]
        self.proxys = db.proxys

    def insert(self, condition, value):
        '''

        :param condition: the condition to find
        :param value:  insert proxy message
        :return:
        '''
        if self.find(condition) == False:
            self.proxys.insert(value)
            return True
        else:
            return False

    def find(self, condition):
        '''

        :param condition: the condition to find
        :return:
        '''
        result = self.proxys.find_one(condition)
        if result is not None:
            return True
        else:
            return False

    def delete(self, condition):
        '''

        :param condition: the condition to delete
        :return:
        '''
        self.proxys.remove(condition)

    def updateID(self):
        proxys = self.proxys.find()
        proxyID = 1
        for proxy in proxys:
            ip = proxy['ip']
            port = proxy['port']
            self.proxys.update({'ip': ip, 'port': port}, {'$set': {'proxyId': proxyID}})
            proxyID += 1