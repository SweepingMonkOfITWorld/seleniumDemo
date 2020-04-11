#coding=utf-8
"""
************************************
--- Author:IT扫地僧 我是高老师
--- File Name:jsdemo.py
--- Date:2020/4/11 8:29
---Developer Tool:PyCharm
************************************
"""
#pip3 install PyExecJS
#PyExecJS库是可以执行js代码
import time
import execjs
with open('./a.js','r',encoding='utf-8') as f:
    js=f.read()
print(execjs.compile(js).call('add', 3, 5))
