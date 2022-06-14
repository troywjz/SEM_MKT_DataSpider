# -*- coding:utf-8 -*-

import BDmkt, SLLmkt, SGmkt, SMmkt
import requests, json, re, time, datetime

date = str(datetime.datetime.now().date())  # 获取当天的日期
# date = '2022-06-14'     # 指定日期
# print(date)   # 查看爬取数据的日期


# 百度账户推广数据
cookie1 = {} # 百度账户的cookie
data1 = {} # 百度账户的data，把其中的日期改为'yyyy-mm-dd'
print('百度账户推广数据：')
try:
    BDmkt.main(date=date, cookie=cookie1, data=data1, location1='A1', location2='B1', location3='C1')
except:
    print('error')


# 360账户推广数据
cookie2 = {}    # 360账户的cookie
print('360账户推广数据：')
try:
    SLLmkt.main(date=date, cookie=cookie2, location1='A2', location2='B2', location3='C2')
except:
    print('error')


# 搜狗账户推广数据
cookie3 = {}    # 搜狗账户的cookie
print('搜狗账户推广数据：')
try:
    SGmkt.main(date=date, cookie=cookie3, location1='A3', location2='B3', location3='C3')
except:
    print('error')


# 神马账户推广数据
cookie4 = {}    # 神马账户的cookie
headers4 = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'uc-csrf-token': '',    # 复制浏览器中的相应字段
    'set-cookie': '',   # 复制浏览器中的相应字段
    'content-type': 'application/json;charset=UTF-8',
}
smid = ''   # 制浏览器中的相应字段
print('神马账户推广数据：')
try:
    SMmkt.main(date=date, cookie=cookie4, headers=headers4, smid=smid, location1='A4', location2='B4', location3='C4')
except:
    print('error')
