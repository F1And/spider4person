# -*- coding: utf-8 -*-
# 配置包：设置

# Scrapy settings for behance project


BOT_NAME = 'behance'

SPIDER_MODULES = ['behance.spiders']
NEWSPIDER_MODULE = 'behance.spiders'


ITEM_PIPELINES = {
   'behance.pipelines.tagPipelines.unsplashPipeline': 300
}

# ITEM_PIPELINES = {
#     'behance.pipelines.tagPipelines.AuthorPipeline': 300
# }




MYSQL_HOST = '127.0.0.1'        # 数据库地址
MYSQL_DBNAME = 'tags'           # 数据库名字
MYSQL_USER = 'root'             # 数据库账号
MYSQL_PASSWD = '123456'         # 数据库密码
MYSQL_PORT = 3306               # 数据库端口