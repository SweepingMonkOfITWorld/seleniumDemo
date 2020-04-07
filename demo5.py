#coding=utf-8
"""
************************************
--- Author:IT扫地僧 我是高老师
--- File Name:demo5.py
--- Date:2020/4/7 16:31
---Developer Tool:PyCharm
************************************
"""
'''
当打开多个窗口时 通过句柄来切换

'''
from selenium import webdriver
import time
chrome_driver=u'C:\\Users\\huawei\\Desktop\\python最新教案\\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver)
#open the url
driver.get("https://www.sina.com.cn")
driver.maximize_window()
time.sleep(2)
firstHand=driver.current_window_handle
driver.find_element_by_link_text('体育').click()
driver.find_element_by_link_text('娱乐').click()
hands=driver.window_handles
for name in hands:
    if name==firstHand:
        driver.switch_to.window(name)
        time.sleep(3)
        driver.close()
time.sleep(3)
driver.quit()