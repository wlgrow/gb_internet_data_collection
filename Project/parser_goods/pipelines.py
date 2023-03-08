from itemadapter import ItemAdapter
from pymongo import MongoClient


class ParserGoodsPipeline:
    def __init__(self):
        client = MongoClient()
        self.mongo_db = client.parser_good

    def process_item(self, item, spider):
        collection = self.mongo_db[spider.name]
        collection.insert_one(item)

        return item
