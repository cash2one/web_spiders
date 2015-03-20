# -*- coding: utf-8 -*-
from doubanmovie.items import DoubanmovieItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy import log
import gl
import doubanapi
import time

class doubanmovieSpider(CrawlSpider):

    name = "doubanmovie"
    start_urls = ['http://movie.douban.com/']
    download_delay = 1.8

    rules = (
        Rule(SgmlLinkExtractor(allow=r'/subject/[0-9]+/\?from'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):

        #log.msg('go into parse_item')
        selector = Selector(response)
        #open('response', 'wb').write(response.body)

        urls=''.join(selector.xpath("//div[@id='recommendations']/div[@class='recommendations-bd']/dl[*]/dt/a/@href").extract())
        #print 'urls:'+urls 
        doubanid_lst= gl.p.findall(urls)

        for doubanid in doubanid_lst:
            log.msg('got doubanid:'+doubanid)
            if doubanid in gl.local_doubanid_lst:
                return
            gl.local_doubanid_lst.append(doubanid)
            movie=DoubanmovieItem()
            movie['movieid']=doubanid
            movie['title'],movie['rating'],movie['nlp_results']=doubanapi.doubanidapi(doubanid)
            yield movie
            time.sleep(0.5)



        
        #i['domain_id'] = hxs.select('//input[@id="sid"]/@value').extract()
        #i['name'] = hxs.select('//div[@id="name"]').extract()
        #i['description'] = hxs.select('//div[@id="description"]').extract()
        

    
