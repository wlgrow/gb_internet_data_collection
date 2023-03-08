# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ParserGoodsItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    price = scrapy.Field()
    brand = scrapy.Field()
    reviews = scrapy.Field()
    presence = scrapy.Field()
    _id = scrapy.Field()

