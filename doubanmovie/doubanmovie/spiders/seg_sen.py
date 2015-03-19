# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 20:55:14 2015

@author: mr007rin
"""
##段落分句
import sys
class seg_sen:
    def __init__(self): 
        print "initialize."
        reload(sys)
        sys.setdefaultencoding('utf8')
    @staticmethod
    def seg(txt):
        txt=txt.strip().replace('？', '。').replace('！', '。').replace('……', '。').replace('\n', '')
        output=txt.split('。')
        return output

