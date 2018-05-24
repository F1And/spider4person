#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 全局包：爬虫字段

import scrapy

class tagItem(scrapy.Item):
    tag_name = scrapy.Field()
    tag_id = scrapy.Field()
    pic_url = scrapy.Field()
    tag_words = scrapy.Field()
    pass

class authorItem(scrapy.Item):
    author_name = scrapy.Field()
    author_url = scrapy.Field()
    pass

class pictureItem(scrapy.Item):
    picture_url = scrapy.Field()
    pass