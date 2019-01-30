# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AirBnbItem(scrapy.Item):
     Title = scrapy.Field()
     Room_type = scrapy.Field()
     num_of_beds = scrapy.Field()
     Price = scrapy.Field()
     Cancel_policy = scrapy.Field()
     Review_stars = scrapy.Field()
     num_of_reviewers = scrapy.Field()

    
