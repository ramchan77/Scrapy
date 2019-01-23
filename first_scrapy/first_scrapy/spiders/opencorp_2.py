# -*- coding: utf-8 -*-
import scrapy


class OpencorpSpider(scrapy.Spider):
    name = 'opencorp_2'
    allowed_domains = ['opencorpdata.com']
    #start_urls = ['https://opencorpdata.com/sg?page=1']
    def start_requests(self):
    	for i in range(5001,10000):
    		yield scrapy.Request("https://opencorpdata.com/sg?page="+str(i),callback=self.parse)
    	

    def parse(self, response):
    	for links in response.xpath('//tr/td[1]/a/@href').extract():
    	    yield { 'link':links }
        pass
