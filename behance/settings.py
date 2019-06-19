# -*- coding: utf-8 -*-
# 配置包：设置

# Scrapy settings for behance project


BOT_NAME = 'behance'

SPIDER_MODULES = ['behance.spiders']
NEWSPIDER_MODULE = 'behance.spiders'


ITEM_PIPELINES = {
   'behance.pipelines.tagPipelines.zcoolPipeline': 500,
   'behance.pipelines.tagPipelines.jobPipeline': 400,
   'behance.pipelines.tagPipelines.picturePipeline': 300,
}


DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    'behance.middleware.ProxyMiddleware': 100,
}

DOWNLOAD_TIMEOUT = 360

MYSQL_HOST = '127.0.0.1'        # 数据库地址
MYSQL_DBNAME = 'images'           # 数据库名字
MYSQL_USER = 'root'             # 数据库账号
MYSQL_PASSWD = '123456'         # 数据库密码
MYSQL_PORT = 53306               # 数据库端口