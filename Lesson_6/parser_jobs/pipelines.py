from itemadapter import ItemAdapter
from pymongo import MongoClient


class ParserJobsPipeline:
    def __init__(self):
        client = MongoClient()
        self.mongo_db = client.parser_jobs

    def process_item(self, item, spider):
        collection = self.mongo_db[spider.name]
        collection.insert_one(item)

        # print('\n**********\n%s\n%s\n***********\n' %(
        #     item,
        #     spider
        # ))
        return item
