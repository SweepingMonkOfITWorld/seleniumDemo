#coding=utf-8
"""
************************************
--- Author:IT扫地僧 我是高老师
--- File Name:demo.py
--- Date:2020/4/6 11:56
---Developer Tool:PyCharm
************************************
"""
from selenium import webdriver
import time
chrome_driver=u'C:\\Users\\huawei\\Desktop\\python最新教案\\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver)
# driver.fullscreen_window() windows不需要此步骤 全屏
driver.implicitly_wait(1)
driver.get("https://www.google.com/")
# driver.find_element_by_css_selector('#gbw > div > div > div.gb_de.gb_i.gb_Cg.gb_tg > div:nth-child(1) > a').click()
driver.find_element_by_css_selector('#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input').send_keys('python\n')
# driver.find_element_by_css_selector('#tsf > div:nth-child(2) > div.A8SBwf > div.FPdoLc.tfB0Bf > center > input.gNO89b').click()
time.sleep(3)
driver.back()#返回上一页
#查找xpath 用chrome的插件chropath 8个查找element的方法
driver.find_element_by_link_text('Gmail').click()
time.sleep(3)
driver.quit()