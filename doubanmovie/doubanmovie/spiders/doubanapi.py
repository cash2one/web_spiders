# -*- coding:utf8 -*-
import urllib2
import json
from seg_sen import seg_sen
def nlp(text):
    url_get_base = "http://ltpapi.voicecloud.cn/analysis/?"
    api_key = 'B3l170O7hW1qqMWNvCBPWmdlZCALIbEq7rVswpmR'
    format = 'xml'
    pattern = 'all'
    result = urllib2.urlopen("%sapi_key=%s&text=%s&format=%s&pattern=%s" % (url_get_base,api_key,text,format,pattern))
    content = result.read().strip()
    print content
    return content
def doubanidapi(id):
    result = urllib2.urlopen("https://api.douban.com/v2/movie/"+id )
    content = result.read().strip()
    s=json.loads(content)
    title=s['alt_title']
    rating=s['rating']['average']
    summary=s['summary']
    movie_type=s['attrs']['movie_type']
    seg=seg_sen()
    input = seg.seg(summary)
    nlpresult=''
    for txt in input:
        if txt!='':
            nlpresult=nlpresult+nlp(txt)
    return title,rating,nlpresult


    





