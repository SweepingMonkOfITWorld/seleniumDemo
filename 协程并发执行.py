#coding=utf-8
"""
************************************
--- Author:IT扫地僧 我是高老师
--- File Name:协程并发执行.py
--- Date:2020/4/17 20:35
---Developer Tool:PyCharm
************************************
"""
import time
import asyncio
async def accumulate(n):
    result=1
    for i in range(n,1,-1):
        result +=1
        await asyncio.sleep(0.01)
    print(f"-->{n}的累加结果为：{result}")
async def main():
    print(f'程序执行开始于：{time.strftime("%X")}')
    print('-'*30)
    task1=asyncio.create_task(accumulate(800))
    task2=asyncio.create_task(accumulate(500))
    task3=asyncio.create_task(accumulate(100))
    await task1
    await task2
    await task3
    print(f'程序执行结束于：{time.strftime("%X")}')
    print('-'*30)
asyncio.run(main())
