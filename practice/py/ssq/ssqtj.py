#! /usr/bin/python3

import logging
import os
import bs4
import time
import openpyxl
import requests

#设置日志
logging.disable(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# 创建目录
path = r'C:\双色球'
if not os.path.exists(path):
    os.makedirs(path)

# 初始化结果Excel
filename = path + 'ssq_new_' + time.strftime('%Y%m%d%H%M%S', time.localtime()) + '.xlsx'
resFile = openpyxl.Workbook()
sheet = resFile.active
sheet.title = "历史双色球统计结果"
sheet['A1'] = "红号列表"
sheet['B1'] = "出现次数"
sheet['C1'] = "蓝号列表"
sheet['D1'] = "出现次数"
sheet['E1'] = "历届开奖"
row_num = 2

# 表格初始化
for idx in range(1, 34):
    sheet['A' + str(idx + 1)] = idx
    sheet['B' + str(idx + 1)] = 0
    if idx < 17:
        sheet['C' + str(idx + 1)] = idx
        sheet['D' + str(idx + 1)] = 0

# resFile.save(path + '\\' + 'movfy_20191110.xlsx')

# 主页面爬取
res = requests.get("http://kaijiang.500.com/ssq.shtml")
res.raise_for_status()

# 解析所有分页列表
soap = bs4.BeautifulSoup(res.text.encode('iso-8859-1'), "html.parser")
sfy = soap.select('span div a')
print('共' + str(len(sfy)) + '期' )

headers1 = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
headers2={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}

# 循环所有分页
for idx in range(len(sfy)):
# for idx in range(2):
    redlist = ''
    suburl = sfy[idx].get('href')
    subtxt = sfy[idx].getText()
    logging.info(suburl)

    # 防止服务器反爬主动断开，每次换不同的
    if idx % 2 == 0:
        head = headers2
    else:
        head = headers1
    time.sleep(0.1)

    # 子页面爬取
    subres = requests.get(suburl, head)
    subres.raise_for_status()

# 解析子页面
    subsoap = bs4.BeautifulSoup(subres.text.encode('iso-8859-1'), "html.parser")
    sublist = subsoap.select('tr td div ul li')

    # 解析红蓝号
    for subidx in range(6):
        # 红号
        red_no = sublist[subidx].getText()
        redlist += sublist[subidx].getText() + ' '
        # print(red_no)
        if red_no.isdigit() is True:
            # print(len(red_no))
            red_idx = int(red_no)
            sheet['B' + str(red_idx + 1)].value += 1

    # 蓝号
    blue_no = sublist[6].getText()
    if len(blue_no) > 0:
        blue_idx = int(blue_no)
        sheet['D' + str(blue_idx + 1)].value += 1

    result = "第" + sfy[idx].getText() + "期：" + redlist + '| ' + blue_no
    # print(result)
    sheet['E' + str(idx + 2)] = result
    resFile.save(filename)

resFile.save(filename)
