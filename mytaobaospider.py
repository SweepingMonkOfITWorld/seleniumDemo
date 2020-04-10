#coding=utf-8
"""
************************************
--- Author:IT扫地僧 我是高老师
--- File Name:taobaospider.py
--- Date:2020/4/9 18:11
---Developer Tool:PyCharm
************************************
"""
from selenium import webdriver
import time
import re
import xlwt
def search_product():
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="q"]').send_keys(kw+'\n')
    time.sleep(15)
    #手机淘宝app扫码登录
    token=driver.find_element_by_xpath('//*[@id="mainsrp-pager"]/div/div/div/div[1]').text
    token=int(re.compile('(\d+)').search(token).group(1))
    return token
#拉动滚动条 加载全部页面元素 防止查找元素时页面还没加载
def drop_down():
    for x in range(1,11,2):
        time.sleep(0.5)
        #j代表滚动条的位置
        j=x/10
        js='document.documentElement.scrollTop=document.documentElement.scrollHeight*%f'%j
        driver.execute_script(js)
def get_product():
    divs=driver.find_elements_by_xpath('//div[@class="items"]/div[@class="item J_MouserOnverReq  "]')
    for div in divs:
        img=div.find_element_by_xpath('.//a/img').get_attribute('src')
        pay_count=div.find_element_by_xpath('.//div[@class="deal-cnt"]').text
        title=div.find_element_by_xpath('.//div[@class="row row-2 title"]/a').text
        title_url=div.find_element_by_xpath('.//div[@class="row row-2 title"]/a').get_attribute('href')
        shop=div.find_element_by_xpath('.//div[@class="shop"]/a').text
        location=div.find_element_by_xpath('.//div[@class="row row-3 g-clearfix"]/div[@class="location"]').text
        price=div.find_element_by_xpath('.//div[@class="price g_price g_price-highlight"]/strong').text
        dct={'商品':title,'价格':price,'购买人数':pay_count,'商家':shop,'地址':location,'图片':img}
        print(dct)
        product_list.append(dct)

def next_page():
    token=search_product()
    # token=3
    drop_down()
    get_product()
    num=1
    while num !=token:
        driver.get('https://s.taobao.com/search?q={0}&s={1}'.format(kw,44*num))
        #隐式等待 最高时间10秒不是强制等待 如果超出报错
        driver.implicitly_wait(10)
        num +=1
        drop_down()
        print(f'********************第{num}页{kw}商品：********************')
        get_product()
        print('-'*200)
def writeExcel(excelPath, lst):
    workbook = xlwt.Workbook()
    # 获取第一个sheet页
    sheet = workbook.add_sheet(kw)
    row0 = ['商品', '价格', '购买人数', '商家', '地址', '图片']
    for i in range(0, len(row0)):
        sheet.write(0, i, row0[i])
    for i in range(0, len(lst)):
        product = lst[i]
        for j in range(0, len(product)):
            sheet.write(i + 1, j, product[row0[j]])
    workbook.save(excelPath)
if __name__ == '__main__':
    kw = input('输入你要搜索的商品：')
    product_list = []
    chrome_driver = u'C:\\Users\\huawei\\Desktop\\python最新教案\\chromedriver_win32\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=chrome_driver)
    driver.maximize_window()
    driver.get(r'http://www.taobao.com')
    next_page()
    writeExcel(f'./{kw}产品明细.xls',product_list)

