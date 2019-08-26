# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem


class TcentSpider(scrapy.Spider):
    name = 'tcent'
    # allowed_domains = ['careers.tencent.com/']
    # start_urls = ['http://www.careers.tencent.com/']

    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
    }


    #  构造url池的方式一 拼接url  index每次加1
    index = 1
    base_url = "https://careers.tencent.com/search.html?index="
    start_urls = [base_url + str(index)]

    #  直接获取下一页的url

    def parse(self, response):
        # 提取每个response 的数据
        # print(response.body)
        node_list = response.xpath("//a[@class='recruit-list-link'] | //p[@class='recruit-tips']"
                                   "| //p[@class='recruit-text']")
        for node in node_list:
            item = TencentItem()
            print(11111111111111111111111111111)
            # 提取每个职位的信息，并将Unicode字符串转化为uft-8
            positionName = node.xpath("./h4/text()").extract()
            workLocation = node.xpath("./span[2]/text()").extract()
            positioType = node.xpath("./span[3]/text()").extract()
            publishData = node.xpath("./span[4]/text()").extract()
            # positionDescript = node.xpath("./p[@class='recruit-text']/text()").extract()
            item["positionName"] = positionName[0].encode("utf-8")
            if len(workLocation):
                item["workLocation"] = workLocation[0].encode("utf-8")
            else:
                item["workLocation"] = "Null"
            if len(positioType):
                item["positioType"] = positioType[0].encode("utf-8")
            else:
                item["positioType"] = "Null"
            item["publishData"] = publishData[0].encode("utf-8")
            # item["positionDescript"] = positionDescript[0].encode("utf-8")
            print(item)

            yield item  # 将字段交给管道处理

        # 以下方式1.页面中没有点击下一页按钮 2.拿的是json，通过翻页来拿的数据
        if self.index < 479:
            self.index += 10
            url = self.base_url + str(self.index)
            # 发送请求
            yield scrapy.Request(url, callback=self.parse)  # 将处理下一页的请求交给调度器


        # 如果页面中(response中)直接能获取到翻页的url或者获取翻页url 的后半部分
        # 规律 最后一页 //a[@class='noactive' and @id='next']  下一页按钮不能点击
        # 规律 第一页 //a[@class='noactive' and @id='pre']  上一页按钮不能点击
        # 规律  中间页  //a[@id='pre']

        # 直接从response 中提取链接，并发送请求处理，直到连接全部提取完
        # if not len(response.xpath("//a[@class='noactive' and @id='next']")):
        #     url = response.xpath("//a[@id='next']/@href").extract()[0]
        #     yield scrapy.Request("https://careers.tencent.com/"+url, callback=self.parse, headers=self.headers)



    #         # 页面类型不相同也可以自己定义函数来处理请求，接受响应
    #     #         scrapy.Request(url, callback=self.next_parse)
    #     #
    #     # def next_parse(self, response):
    #     #     pass
