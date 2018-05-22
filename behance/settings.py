# -*- coding: utf-8 -*-

# Scrapy settings for behance project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'behance'

SPIDER_MODULES = ['behance.spiders']
NEWSPIDER_MODULE = 'behance.spiders'


ITEM_PIPELINES = {
   'behance.pipelines.tagPipelines.BehancePipeline': 300
}

# ITEM_PIPELINES = {
#     'behance.pipelines.tagPipelines.AuthorPipeline': 300
# }





MYSQL_HOST = '127.0.0.1'        # 数据库地址
MYSQL_DBNAME = 'tags'           # 数据库名字
MYSQL_USER = 'root'             # 数据库账号
MYSQL_PASSWD = '123456'         # 数据库密码

MYSQL_PORT = 3306               # 数据库端口，在dbhelper中使用