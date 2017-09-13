# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyprojectItem(scrapy.Item):
    # 小说的名字
    name = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 小说的地址
    novelurl = scrapy.Field()
    # 状态
    serialstatus = scrapy.Field()
    # 连载字数
    serialnumber = scrapy.Field()
    # 文章类别
    category = scrapy.Field()
    # 小说编号
    name_id = scrapy.Field()
