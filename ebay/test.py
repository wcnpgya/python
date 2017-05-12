# coding=utf8

import requests
import json

head = {'User-Agent': \
            'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'}

jscontent = requests.get('http://www.ebay.com/sch/Feeding/20400/i.html?_ssan=Brand',
                         headers=head).content
jsDict = json.loads(jscontent)
jsvalues = jsDict['values']
i = 0
for each in jsvalues:
    print each['title']
    i += 1
    print i