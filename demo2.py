#coding=utf-8
"""
************************************
--- Author:IT扫地僧 我是高老师
--- File Name:demo2.py
--- Date:2020/4/6 20:39
---Developer Tool:PyCharm
************************************
"""
from selenium import webdriver
import time
chrome_driver=u'C:\\Users\\huawei\\Desktop\\python最新教案\\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver)
#open the url
driver.get("https://www.baidu.com")
#maxium the browser
driver.maximize_window()
time.sleep(2)
# get title
print(driver.title)
#get current url
print(driver.current_url)
#browser refresh
time.sleep(2)
driver.refresh()
#open anothor url
driver.get('http://www.ifeng.com')
time.sleep(2)
#browser back
driver.back()
time.sleep(2)
#browser forward
driver.forward()
time.sleep(2)
#get page source
print(driver.page_source)
#browser close/quit 如果有多个标签窗口close()关闭当前窗口  quit()全部关闭
driver.quit()
