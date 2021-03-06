# -*- coding: utf-8 -*-

# Scrapy settings for zhihu project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'zhihu'

SPIDER_MODULES = ['zhihu.spiders']
NEWSPIDER_MODULE = 'zhihu.spiders'
ITEM_PIPELINES = {
    'zhihu.pipelines.ZhihuPipeline':300
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhihu (+http://www.yourdomain.com)'

HEADER={
    "Host": "www.zhihu.com",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36",
    "Referer": "http://www.zhihu.com/people/raymond-wang",
    "Accept-Encoding": "gzip,deflate,sdch",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2",
    }

COOKIES={
    '__utma':r'51854390.164469527.1358498147.1425624113.1425626962.54',
    '__utmb':r'51854390.5.10.1425626962',
    '__utmc':r'51854390',
    '__utmt':r'1',
    '__utmv':r'51854390.100--|2=registration_date=20150306=1^3=entry_date=20140721=1',
    '__utmz':r'51854390.1425626962.54.12.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/topic',
    '_xsrf':r'13103537912dcc9130815a1827a23288',
    'c_c':r'a3076532c3d211e48aff52540a3121f7',
    'q_c1':r'6061178aea6643f5b7cd3421df372bad|1425256446000|1405926861000',
    'r_c':r'1',
    'z_c0':r'"QUtBQTl6S1R1d2NYQUFBQVlRSlZUWlhrSUZWSnNFcFd0Q0JwR1FmSjJEZ2wwTG9lcDRWam9RPT0=|1425627029|b560cf4618606b220a6731fab36ebb867b7f070a"',
    'zata':r'zhihu.com.182ed52a34fe482dac2dbc214694bfbc.637977'
    }

