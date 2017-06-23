# -*- coding: utf-8 -*-
import scrapy
import json
from Douyu.items import DouyuItem

class DouyuSpider(scrapy.Spider):
    # 在这个类中定义的方法实际上和在__init__中定义的一样，使用时候加上self
    name = "douyu"
    allowed_domains = ["capi.douyucdn.cn"]
    
    offset = 0
    baseURL = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    start_urls = ( baseURL + str(offset),)

    def parse(self, response):
        # response返回的是json，需要进行处理
        #body得到html字符串,load和本地磁盘交互，ｌｏａｄｓ和字符串交互
        data_list = json.loads(response.body)['data']
        if len(data_list):
            # print data
            for data in data_list:
                item = DouyuItem()
                item['nickname'] = data['nickname']
                item['imagelink'] = data['vertical_src']

                yield item
                # print '=================='
            #上面处理完成后，重新用scrapy发送请求，可以通过判断data的元素
            #是否为空进行判断

            self.offset += 20
            yield scrapy.Request(self.baseURL+str(self.offset), callback=self.parse)
        else:
            return


