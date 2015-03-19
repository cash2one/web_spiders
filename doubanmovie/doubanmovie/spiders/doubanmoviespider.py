# -*- coding: utf-8 -*-
from doubanmovie.items import DoubanmovieItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy import log
import gl
import doubanapi

class doubanmovieSpider(CrawlSpider):

    name = "doubanmovie"
    start_urls = ['http://movie.douban.com/']
    download_delay = 2
    rules = (
        Rule(SgmlLinkExtractor(allow=r'/subject/[0-9]+/\?from'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        log.start(logfile='LOG_FILE')
        #log.msg('go into parse_item')
        selector = Selector(response)
        #open('response', 'wb').write(response.body)

        urls=''.join(selector.xpath("//div[@id='recommendations']/div[@class='recommendations-bd']/dl[*]/dt/a/@href").extract())
        #print 'urls:'+urls 
        doubanid_lst= gl.p.findall(urls)

        for doubanid in doubanid_lst:
            log.msg('got doubanid:'+doubanid)
            movie=DoubanmovieItem()
            movie['id']=doubanid
            movie['title'],movie['rating'],movie['nlp_result']=doubanapi.doubanidapi(doubanid)
            yield movie


        
        #i['domain_id'] = hxs.select('//input[@id="sid"]/@value').extract()
        #i['name'] = hxs.select('//div[@id="name"]').extract()
        #i['description'] = hxs.select('//div[@id="description"]').extract()
        

    
