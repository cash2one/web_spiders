# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class DoubanmovieItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    moviename = Field()
    year= Field()
    #base_info=Field()
    introduction=Field()
    rating=Field()
    url=Field()
    director=Field()
    writer=Field()
    actor=Field()
    rec_urls=Field()
    pass
