#coding=utf-8
"""
************************************
--- Author:IT扫地僧 我是高老师
--- File Name:验证码.py
--- Date:2020/4/11 11:08
---Developer Tool:PyCharm
************************************
"""
import requests
import base64
url='https://kyfw.12306.cn/passport/captcha/captcha-image'
data={
'login_site': 'E',
'module': 'login',
'rand': 'sjrand',
}
session=requests.session()
req=session.get(url,params=data)
with open('yzm.png','wb') as f:
    f.write(req.content)
point_map={
    '1':'45,50',
    '2':'120,50',
    '3':'180,50',
    '4':'260,50',
    '5':'45,120',
    '6':'120,120',
    '7':'180,120',
    '8':'260,120',
}
def get_position(index):
    temp=[]
    for i in index.split(','):
        temp.append(point_map[i])
    return ','.join(temp)

#截图从左上角量坐标
code=get_position(input('输入验证码：'))
check_url='https://kyfw.12306.cn/passport/captcha/captcha-check'
data={
'answer': code,
'rand': 'sjrand',
'login_site': 'E',

}

req=session.get(check_url,params=data)
print(req.content.decode('utf-8'))