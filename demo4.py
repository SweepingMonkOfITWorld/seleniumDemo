#coding=utf-8
"""
************************************
--- Author:IT扫地僧 我是高老师
--- File Name:demo4.py
--- Date:2020/4/6 22:02
---Developer Tool:PyCharm
************************************
"""
from selenium import webdriver
import time
chrome_driver=u'C:\\Users\\huawei\\Desktop\\python最新教案\\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver)
#open the url
driver.get("https://www.baidu.com")
driver.maximize_window()
time.sleep(2)
#进入百度页面截图
driver.save_screenshot('截图.png')
driver.close()