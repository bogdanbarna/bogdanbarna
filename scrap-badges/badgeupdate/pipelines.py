# -*- coding: utf-8 -*-

import json
from itemadapter import ItemAdapter

items = []


class JsonWriterPipeline:
    def open_spider(self, spider):
        self.file = open("items.jl", "r+")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        self.file.write(line)
        return item


class ItemCollectorPipeline:
    def process_item(self, item, spider):
        items.append(item)
