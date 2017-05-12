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

        filename = '%s/%s/' % (settings.IMAGES_STORE, settings.IMAGES_SUB)
        print filename
        targetpath = os.path.dirname(filename)
        if not os.path.isdir(targetpath):
            os.makedirs(targetpath)




# if __name__ == '__main__':
#     handle = MeiziScrapyPipeline()
#     handle.process_item()
        # if not os.path.exists(dir_path):
        #     os.makedirs(dir_path)
            # for image_url in item['image_url']:
            #     us = image_url.split('/')[3:]
            #     image_file_name = '_'.join(us)
            #     file_path = '%s/%s' % (dir_path, image_file_name)
            #     images.append(file_path)
            #     if os.path.exists(file_path):
            #         continue
            #
            #     with open(file_path, 'wb') as handle:
            #         response = requests.get(image_url, stream=True)
            #         for block in response.iter_content(1024):
            #             if not block:
            #                 break
            #
            #             handle.write(block)

