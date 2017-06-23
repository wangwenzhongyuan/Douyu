# -*- coding: utf-8 -*-

from scrapy.pipelines.images import ImagesPipeline
import scrapy
import os
from settings import IMAGES_STORE as images_store

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#不再继承object,而是继承自ImagesPipeline
class DouyuPipeline(ImagesPipeline):
	#获取媒体文件的请求
	#重写父类方法，可以处理请求，返回一个request给下载器下载,request可以写图片的链接
	def get_media_requests(self, item, info):
		# 获取图片链接，返回给管道
		image_link = item['imagelink']
		#返回给管道,发送完之后，由哪个地方存储,
		#setting中有一个很关键的参数：IMAGES_STORE,
		#如果我们继承了imagespipeline,我们下载的图片将默认访问他记录的地址

		yield scrapy.Request(image_link)


	def item_completed(self, results, item, info):
		# print results
	# 	#print "*" * 30
	# 	# 取出results里图片信息中的 图片路径的值
		image_path = [x["path"] for ok, x in results if ok]

		os.rename(images_store + image_path[0], images_store + item["nickname"] + ".jpg")
		
		return item


		# [x['path'] for ok, x in results]

		# [(True, {'url': 'https://rpic.douyucdn.cn/appCovers/2017/06/17/1810124_20170617141255_big.jpg', 'path': 'full/d2d8c14d3ea1a0399098b6bbbcca9f021276db19.jpg', 'checksum': '686e0ade5482dfce4b19b43f994e569a'})]



