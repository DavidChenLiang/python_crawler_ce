import scrapy

from zhihu.settings import EMAIL, PASSWORD

class ZhiHuSpider(scrapy.Spider):
    name = "zhihu"
    start_urls=["http://www.zhihu.com/",]

    def parse(self, response):
        return scrapy.FormRequest.from_response(response,
                formdata={"email": EMAIL, "password": PASSWORD},
                callback=self.after_login,
                method="post",
                url="http://www.zhihu.com/login/email")

    def after_login(self, response):
        return scrapy.Request("https://www.zhihu.com/", self.parse_index)

    def parse_index(self, response):
        for item in response.xpath("//a[@class='question_link']/text()").extract():
            print item
