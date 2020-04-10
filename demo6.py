# coding=utf-8
"""
************************************
--- Author:IT扫地僧 我是高老师
--- File Name:demo6.py
--- Date:2020/4/7 21:56
---Developer Tool:PyCharm
************************************
"""
from selenium import webdriver
import time

chrome_driver = u'C:\\Users\\huawei\\Desktop\\python最新教案\\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver)
# open the url
driver.get(r'C:\Users\huawei\Desktop\python最新教案\selenium教程\html\a.html')
driver.maximize_window()
driver.implicitly_wait(3)
driver.find_element_by_id('alert').click()
alert = driver.switch_to.alert
print(alert.text)
time.sleep(3)
alert.accept()
time.sleep(3)
driver.find_element_by_id('confirm').click()
confirm = driver.switch_to.alert
time.sleep(3)
confirm.dismiss()
time.sleep(3)
driver.quit()
