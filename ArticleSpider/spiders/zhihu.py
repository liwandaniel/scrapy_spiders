# -*- coding: utf-8 -*-
import scrapy
import re
import json
# import urllib
import os
# import requests
try:
    import cookielib
except:
    import http.cookiejar as cookielib


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']
    agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"
    headers = {
        "HOST": "www.zhihu.com",
        "Referer": "https://www.zhihu.com",
        'User-Agent': agent
    }

    def parse(self, response):
        pass

    def start_requests(self):
        return [scrapy.Request('https://www.zhihu.com/#signin', headers=self.headers, callback=self.login)]

    # def get_captcha(self, response):
    #     import time
    #     captcha_url = 'http://www.zhihu.com/captcha.gif?r=%d&type=login' % (time.time() * 1000)
    #     # 准备下载验证码
    #     with open('captcha.jpg', 'wb') as f:
    #         f.write(captcha_url)
    #     from PIL import Image
    #     try:
    #         im = Image.open("captcha.jpg")
    #         im.show()
    #         im.close()
    #     except:
    #         pass
    #     captcha = input("输入验证码\n>")
    #     return [scrapy.Request(url=captcha_url, headers=self.headers, callback=self.login)]
        # yield scrapy.Request(
        #     url=captcha_url,
        #     headers=self.headers,
        #     meta={
        #         'proxy': UsersConfig['proxy'],
        #         'cookiejar': response.meta['cookiejar'],
        #         '_xsrf': _xsrf
        #     },
        #     callback=self.download_captcha
        # )


# def get_captcha(self, response):
#         import time
#         response_text = response.text
#         captcha_content = response.get('http://www.zhihu.com/captcha.gif?r=%d&type=login' % (time.time() * 1000),
#                                       headers=self.headers).content
#         with open("captcha.jpg", "wb") as f:
#             f.write(captcha_content)
#             f.close()
#
#         from PIL import Image
#         try:
#             im = Image.open("captcha.jpg")
#             im.show()
#             im.close()
#         except:
#             pass
#         captcha = input("输入验证码\n>")
#         return [scrapy.Request(captcha, callback=self.login)]



    def login(self, response):
        response_text = response.text
        pattern = r'name="_xsrf" value="(.*?)"'
        _xsrf = re.findall(pattern, response_text)
        xsrf = _xsrf[0]
        print(xsrf)

        if xsrf:
            post_data = {
                "_xsrf": xsrf,
                "phone_num": "18267728867",
                "password": "liwan/.,1993",
                "captcha": "",
            }
            import time
            # t = str(int(time.time() * 1000))
            # 'http://www.zhihu.com/captcha.gif?r=%d&type=login' % (time.time() * 1000)
            captcha_url = 'http://www.zhihu.com/captcha.gif?r=%d&type=login' % (time.time() * 1000)
            yield scrapy.Request(captcha_url, headers=self.headers, meta={"post_data": post_data}, callback=self.login_after_captcha)

    def login_after_captcha(self, response):
        with open("captcha.jpg", "wb") as f:
            f.write(response.body)
            f.close()

        from PIL import Image
        try:
            im = Image.open("captcha.jpg")
            im.show()
            im.close()
        except:
            pass
        captcha = input("输入验证码\n>")
        post_data = response.meta.get("post_data", {})
        post_url = "https://www.zhihu.com/login/phone_num"
        post_data["captcha"] = captcha
        return [scrapy.FormRequest(
            url=post_url,
            formdata=post_data,
            headers=self.headers,
            callback=self.check_login,

        )]

    def check_login(self, response):
        #验证服务器的返回数据判断是否成功
        text_json = json.loads(response.text)
        if "msg" in text_json and text_json["msg"] == "登录成功":
            for url in self.start_urls:
                yield scrapy.Request(url, dont_filter=True, headers=self.headers)
