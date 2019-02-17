#Uniform interface for all parser modules
import json
import requests
import html2text
import datetime
from parser_interface import Parser
from pprint import pprint
from enum import Enum


class BashFilter:
    RANDOM = '/random/'
    NEW = '/'
    BEST = '/best/'
    BESTYEAR2018 = '/bestyear/2018/'
    BESTYEAR2017 = '/bestyear/2017/'
    BESTYEAR2016 = '/bestyear/2016/'
    BESTYEAR2015 = '/bestyear/2015/'
    BESTYEAR2014 = '/bestyear/2014/'
    BESTYEAR2013 = '/bestyear/2013/'
    BESTYEAR2012 = '/bestyear/2012/'
    BESTYEAR2011 = '/bestyear/2011/'
    BESTYEAR2004 = '/bestyear/2004/'
    BESTYEAR2005 = '/bestyear/2005/'
    BESTYEAR2006 = '/bestyear/2006/'
    BESTYEAR2007 = '/bestyear/2007/'
    BESTYEAR2008 = '/bestyear/2008/'
    BESTYEAR2009 = '/bestyear/2009/'


class ParserBash(Parser):

    def __init__(self):
       Parser.__init__(self)
    #following methods are ment to be implemented

    def parse(self, filter_ = str(BashFilter.RANDOM)):
        
        begin = 0
        url = 'https://bash.im' + filter_
        r = requests.get(url)
        while(True):
        
            i = r.text.find('class="id">#',begin)
            k = r.text.find('</a>',i)
            id_ = html2text.html2text(r.text[i+12:k+4])

            if id_ == '\n\n':
                break

            i = r.text.find('class="rating">',begin)
            k = r.text.find('</span>',i)
            rate = html2text.html2text(r.text[i+15:k+7])

            i = r.text.find('<span class="date">',begin)
            k = r.text.find('</span>',i)
            date = html2text.html2text(r.text[i+19:k+8])

            i = r.text.find('<div class="text">',begin)
            k = r.text.find('</div>',i)
            joke = html2text.html2text(r.text[i:k+6])
            
            begin = k+8

            self.content.next()
            self.content.set_source_name('bash.im')
            self.content.set_text(joke)
            self.content.set_id(int(id_))
            self.content.set_rate(int(rate))
            self.content.set_time(date)
            self.content.set_url('https://bash.im/quote/' + str(id_)+'/')

        return self.content.get_content_table()

parser_bash = ParserBash()
pprint(parser_bash.parse())