# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ParserJobsItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    min_salary = scrapy.Field()
    max_salary = scrapy.Field()
    _id = scrapy.Field()
