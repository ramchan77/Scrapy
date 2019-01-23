# -*- coding: utf-8 -*-
import scrapy


class OpencorpSpider(scrapy.Spider):
    name = 'opencorp'
    allowed_domains = ['hoovers.com']
    def start_requests(self):
        start_urls = ['http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=1',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=2',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=3',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=4',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=5',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=6',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=7',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=8',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=9',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=0',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=11',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=12',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=13',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=14',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=15',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=16',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=17',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=18',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=19',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=20',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=21',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=22',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=23',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=24',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=25',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=26',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=27',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=28',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=29',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=30',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=31',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=32',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=33',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=34',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=35',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=36',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=37',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=38',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=39',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=40',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=41',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=42',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=43',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=44',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=45',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=46',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=47',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=48',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=49',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=50',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=51',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=52',
                    'http://www.hoovers.com/company-information/company-search.html?nvcnt=65&nvemp=[;200]&nvind=1518&sortDir=Descending&sort=SalesUS&maxitems=100&page=53']        
    	for i in start_urls:
    		yield scrapy.Request(i,callback=self.parse)
    	

    def parse(self, response):
    	for links in response.xpath('//tr/td[1]/a/@href').extract():
    	    yield { 'link':links }
        pass
