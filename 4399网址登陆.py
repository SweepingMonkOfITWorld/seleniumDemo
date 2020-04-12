#coding=utf-8
"""
************************************
--- Author:IT扫地僧 我是高老师
--- File Name:4399网址登陆.py
--- Date:2020/4/12 10:37
---Developer Tool:PyCharm
************************************
"""
from selenium import webdriver
from PIL import Image
def click_login():
    driver.find_element_by_id('login_tologin').click()
def screenshot(pic,ele,savepath):
    frame_left = ele.location['x']
    frame_top = ele.location['y']
    frame_right = ele.size['width'] + frame_left
    frame_bottom = ele.size['height'] + frame_top
    # print(frame_left, frame_top, frame_right, frame_bottom)
    img = Image.open(pic)
    img = img.crop((frame_left, frame_top, frame_right, frame_bottom))
    img.save(savepath)
    
def login():
    # 截图的目的是把验证码的图截出来
    driver.save_screenshot('full.png')
    login_frame = driver.find_element_by_id('popup_login_frame')
    screenshot('full.png',login_frame,'login.png')
    #切换到iframe框架
    driver.switch_to.frame('popup_login_frame')
    yzm_element=driver.find_element_by_id('captcha')
    screenshot('login.png',yzm_element,'yzm.png')
if __name__ == '__main__':
    chrome_driver = r'C:\Users\huawei\Desktop\python最新教案\chromedriver_win32\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=chrome_driver)
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(r'http://www.4399.com')
    click_login()
    login()