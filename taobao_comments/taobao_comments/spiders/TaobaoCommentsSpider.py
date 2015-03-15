#coding:utf-8

from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from taobao_comments.items import TaobaoCommentsItem



host='http://www.taobao.com'

class TaobaoCommentsSpider(CrawlSpider):
    name = 'TaobaoComments'
    allowed_domains = ['tmall.com']
    start_urls = [
        "http://detail.tmall.com/item.htm?id=16204910274",
        ]

    #使用rule时候，不要定义parse方法
    rules = (
        Rule(SgmlLinkExtractor(allow=("/item.htm?.+", )),  callback='parse_item')
    )

    def __init__(self,  *a,  **kwargs):
        super(TaobaoCommentsSpider, self)
        self.user_names = []

    
    
    def parse_item(self, response):
        print 'run into parse_item'
        selector = Selector(response)
        cmts = TaobaoCommentsItem()
        cmts['url']= response.url
        cmts['comment'] = []
        for node in selector.xpath('//div[@class=\'tm-rate-content\']/div[@class=\'tm-rate-fulltxt\']').extract():
           print node
           
       