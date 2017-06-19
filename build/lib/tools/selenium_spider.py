# _*_ coding: utf-8 _*_

from selenium import webdriver
from scrapy.selector import Selector


# browser.get("https://www.zhihu.com/signin")
#
# browser.find_element_by_css_selector(".view-signin input[name='account']").send_keys("18267728867")
# browser.find_element_by_css_selector(".view-signin input[name='password']").send_keys("liwan/123.,1993")
# browser.find_element_by_css_selector(".view-signin button.sign-button").click()

# selenium完成微博模拟登录
# browser.get("https://www.oschina.net/blog")
# import time
# time.sleep(10)
# # browser.find_element_by_css_selector("#loginname").send_keys("18267728867")
# # browser.find_element_by_css_selector(".info_list input[name='password']").send_keys("liwan/123")
# # browser.find_element_by_css_selector(".info_list login_btn a[node-type=submitBtn]").click()
#
#用selenium实现JavaScript脚本原生代码鼠标下拉
# for i in range(3):
#     browser.execute_script("window.scrollTo(0, document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;")
#     time.sleep(3)

# t_selector = Selector(text=browser.page_source)

#设置chromedriver不加载图片，设置不加载图片可以加速页面的加载，从而提高爬虫的效率
# Chrome_opt = webdriver.ChromeOptions()
# prefs = {"profile.managed_default_content_settings.images": 2}
# Chrome_opt.add_experimental_option("prefs", prefs)
# browser = webdriver.Chrome(executable_path="/home/daniel/scrapy/ArticleSpider/chromedriver", chrome_options=Chrome_opt)
# browser.get("https://www.tmall.com/")

#phantomjs，无界面的浏览器，多进程情况下phantomjs的性能会下降很严重
browser = webdriver.PhantomJS(executable_path="/home/daniel/scrapy/ArticleSpider/phantomjs-2.1.1-linux-x86_64/bin/phantomjs")
browser.get("https://www.tmall.com/")
print(browser.page_source)
browser.quit()



