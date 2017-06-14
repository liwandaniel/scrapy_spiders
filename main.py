# _*_ coding: utf-8 _*_

from scrapy.cmdline import execute
import sys
import os


sys.path.append(os.path.dirname(os.path.abspath(__file__)))  #获取main文件的目录的父目录
# execute(["scrapy", "crawl", "jobbole"])
# execute(["scrapy", "crawl", "zhihu"])
execute(["scrapy", "crawl", "lagou"])