# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json


class JsonWriterPipeline(object):
    def __init__(self):
        self.result = []

    def open_spider(self, spider):
        self.result = []

    def close_spider(self, spider):

        with open('scraped_items.json', 'w') as file:
            text = json.dumps(
                self.result,
                indent=4,
                separators=(',', ': '),
                ensure_ascii=False
            )
            file.write(text)

        self.result = []

    def process_item(self, item, spider):
        self.result.append(item)

        return item


class MainPipeline(object):
    def process_item(self, item, spider):
        return item