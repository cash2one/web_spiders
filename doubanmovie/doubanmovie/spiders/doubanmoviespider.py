# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from scrapy.http import Request
from doubanmovie.items import DoubanmovieItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
import time

class doubanmovieSpider(CrawlSpider):
    name = "doubanmovie"
    start_urls = ['http://movie.douban.com/']
    download_delay = 2
    rules = (
        Rule(SgmlLinkExtractor(allow=r'/subject/[0-9]+/\?from'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        #log.start(logfile='LOG_FILE')
        #log.msg('go into parse_item')
        selector = Selector(response)
        #open('response', 'wb').write(response.body)
        movie=DoubanmovieItem()
        movie['moviename']=''.join(selector.xpath("//div[@id='content']/h1/span[1]/text()").extract())
        #log.msg('moviename:'+movie['moviename'])
        yield movie
        
        #i['domain_id'] = hxs.select('//input[@id="sid"]/@value').extract()
        #i['name'] = hxs.select('//div[@id="name"]').extract()
        #i['description'] = hxs.select('//div[@id="description"]').extract()
        

    
