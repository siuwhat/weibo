# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeiboItem(scrapy.Item):
    USERNAME=scrapy.Field()
    USERID=scrapy.Field()
    LOCATION=scrapy.Field()
    IPREGION=scrapy.Field()
    TIME=scrapy.Field()
    TEXT=scrapy.Field()


