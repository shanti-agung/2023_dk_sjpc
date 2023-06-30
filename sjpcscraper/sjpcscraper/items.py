# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SjpcscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class RptFieldItem(scrapy.Item):
    category    = scrapy.Field()
    rpt_name    = scrapy.Field()
    field_name  = scrapy.Field()
    data_type   = scrapy.Field()
    notes       = scrapy.Field()
