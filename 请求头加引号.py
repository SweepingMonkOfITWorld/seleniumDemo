#coding=utf-8
"""
************************************
--- Author:IT扫地僧 我是高老师
--- File Name:请求头加引号.py
--- Date:2020/4/11 11:00
---Developer Tool:PyCharm
************************************
"""
import re
headers_str="""
answer: 172,110,116,38
rand: sjrand
login_site: E

"""
pattern='^(.*?): (.*)$'
for line in headers_str.splitlines():
    print(re.sub(pattern,'\'\\1\': \'\\2\',',line))