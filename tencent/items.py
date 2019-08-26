# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    positionName = scrapy.Field()  # 职位名
    # positionLink = scrapy.Field()  # 详情页链接
    workLocation = scrapy.Field()  # 工作地点
    positioType = scrapy.Field()  # 职位类别
    publishData = scrapy.Field()  # 发布日期
    # positionDescript = scrapy.Field()  # 简介
