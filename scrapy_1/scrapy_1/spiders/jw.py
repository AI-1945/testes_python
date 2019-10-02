# -*- coding: utf-8 -*-
import scrapy


class JwSpider(scrapy.Spider):
    name = 'jw'
    allowed_domains = ['jw.org']
    start_urls = ['http://jw.org/']

    def parse(self, response):
        pass
