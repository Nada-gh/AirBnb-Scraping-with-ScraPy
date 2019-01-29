# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AirBnbItem(scrapy.Item):
    # define the fields for your item here like:
    Title = scrapy.Field()
    room_type = scrapy.Field()
    num_of_beds = scrapy.Field()
    price = scrapy.Field()


