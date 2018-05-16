#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 执行包：运行爬虫

from scrapy import cmdline

# name = 'portfolio'
name = 'type'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())
