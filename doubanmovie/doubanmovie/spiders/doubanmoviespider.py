# -*- coding: utf-8 -*-
from doubanmovie.items import DoubanmovieItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

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
        movie['url']=response.url
        movie['moviename']=''.join(selector.xpath("//div[@id='content']/h1/span[1]/text()").extract())
        movie['year']=''.join(selector.xpath("//div[@id='content']/h1/span[@class='year']/text()").extract()).replace("(","").replace(")","")
        movie['director']=''.join(selector.xpath("//div[@id='info']/span[1]/span[@class='attrs']/a/text()").extract())
        movie['writer']=''.join(selector.xpath("//div[@id='info']/span[2]/span[@class='attrs']/a/text()").extract())
        movie['actor']=''.join(selector.xpath("//div[@id='info']/span[@class='actor']/span[@class='attrs']").extract())
        movie['introduction']=''.join(selector.xpath("//div[@id='link-report']/span[1]/text()").extract()).replace(" ","")
        movie['rating']=''.join(selector.xpath("//div[@class='rating_wrap clearbox']/p[@class='rating_self clearfix']/strong[@class='ll rating_num']/text()").extract())
        #log.msg('moviename:'+movie['moviename'])
        yield movie
        
        #i['domain_id'] = hxs.select('//input[@id="sid"]/@value').extract()
        #i['name'] = hxs.select('//div[@id="name"]').extract()
        #i['description'] = hxs.select('//div[@id="description"]').extract()
        

    
