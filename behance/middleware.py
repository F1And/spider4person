#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 全局包：数据库配置

class ProxyMiddleware(object):

    def process_request(self, request, spider):
        spider.logger.info("behanceSpiderMiddleware")
        request.meta['proxy'] = "http://127.0.0.1:1080"
        spider.logger.info("request.meta % s", request.meta)
