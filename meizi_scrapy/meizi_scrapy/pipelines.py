# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests
from meizi_scrapy import settings
import os

class MeiziScrapyPipeline(object):
    def process_item(self, item, spider):

        if 'image_url' in item:
            urls = [] #strorage aimurl
            print item['image_name'][0]
            # print item['image_url'][0]
            # print int(item['page_total_num'][0])
            subFileName = item['image_name'][0]
            page = int(item['page_total_num'][0])
            temp_url = item['image_url'][0]
            #modify url
            us = temp_url.split('/')[2:]
            us.pop()
            a = '/'.join(us)
            for index in range(1, page + 1):
                url = 'http://' + a + '/' + str(index) + '.jpg'
                urls.append(url)
            # print urls

            filename = '%s%s/' % (settings.IMAGE_STORAGE, subFileName)
            if not os.path.exists(filename):
                os.makedirs(filename)

            for image in urls:
                us = image.split('/')[4:]
                image_file_name = '_'.join(us)
                file_path = '%s%s' % (filename, image_file_name)

                if os.path.exists(file_path):
                    continue

                with open(file_path, 'wb') as handle:
                    response = requests.get(image, stream=True)
                    for block in response.iter_content(1024):
                        if not block:
                            break
                        handle.write(block)

        return item
