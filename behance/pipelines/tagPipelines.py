#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 工作包：数据库工作

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from behance.DB.dbHelper import DBHelper

class BehancePipeline(object):
    def __init__(self):
        self.db = DBHelper()

    def process_item(self, item, spider):
        self.db.insert(item)
        return item

class AuthorPipeline(object):
    def __init__(self):
        self.db = DBHelper()

    def process_item(self, item, spider):
        self.db.insert_author(item)
        return item

class zcoolPipeline(object):
    def __init__(self):
        self.db = DBHelper()

    def process_item(self, item, spider):
        self.db.insert_person(item)
        return item

class jobPipeline(object):
    def __init__(self):
        self.db = DBHelper()

    def process_item(self, item, spider):
        self.db.insert_person(item)
        return item

class picturePipeline(object):
    def __init__(self):
        self.db = DBHelper()

    def process_item(self, item, spider):
        self.db.insert_picture(item)
        return item