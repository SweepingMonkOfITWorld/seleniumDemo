#coding=utf-8
"""
************************************
--- Author:IT扫地僧 我是高老师
--- File Name:demo3.py
--- Date:2020/4/6 21:35
---Developer Tool:PyCharm
************************************
"""
#在html中下拉选select是一个比较特殊的控件 selenium有一个Select类来操作下拉选
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
chrome_driver=u'C:\\Users\\huawei\\Desktop\\python最新教案\\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get('https://timeanddate.com')
driver.maximize_window()
time.sleep(2)
selectMonth=driver.find_element_by_id('month')
Select(selectMonth).select_by_value('12')
selectCountry=driver.find_element_by_id('country')
Select(selectCountry).select_by_visible_text('Canada')
time.sleep(2)
driver.find_element_by_xpath('//div[4]//input[1]').click()
time.sleep(2)
driver.quit()
