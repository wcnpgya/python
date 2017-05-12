# coding=utf8
import re
url = 'http://www.ebay.com/sch/Nursery-Bedding-/20416/i.html'
us = url.split('/')
temp = list(us[4])
temp.pop()
result = ''.join(temp)
us[4] = result
rurl = '/'.join(us)
print rurl
