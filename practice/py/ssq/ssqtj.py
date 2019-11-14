#! /usr/bin/python3

import logging
import os
import bs4
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

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
head={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}

# 循环所有分页
for idx in range(50):
# for idx in range(2):
    redlist = ''
    suburl = sfy[idx].get('href')
    logging.info(suburl)
    subres = requests.get(suburl, headers=head)
    subres.raise_for_status()

    # 解析子页面
    subsoap = bs4.BeautifulSoup(subres.text.encode('iso-8859-1'), "html.parser")
    sublist = subsoap.select('tr td div ul li')

    # 解析红蓝号
    for subidx in range(6):
        # 红号
        red_no = sublist[subidx].getText()
        redlist += sublist[subidx].getText() + ' '
        red_idx = int(red_no)
        sheet['B' + str(red_idx + 1)].value += 1

    # 蓝号
    blue_no = sublist[6].getText()
    blue_idx = int(blue_no)
    # print(sheet['D' + str(blue_idx + 1)].value)
    sheet['D' + str(blue_idx + 1)].value += 1
    result = "第" + sfy[idx].getText() + "期：" + redlist + '| ' + blue_no
    print(result)
    sheet['E' + str(idx + 2)] = result

resFile.save(path + '\\' + 'ssq_new.xlsx')
'''# 循环处理单个子页面
    for i in range(len(sublist)):

        if "dyzz" in sublist[i].get('href') or "oumeitv" in sublist[i].get('href'):
            continue
        else:
            # 获取详细页面
            mhtml = "https://www.dy2018.com" + sublist[i].get('href')
            # logging.info(mhtml)
            mres = requests.get(mhtml)
            mres.raise_for_status()
            msoap = bs4.BeautifulSoup(mres.text.encode('iso-8859-1').decode('gbk'), "html.parser")

            # 获取电影名称
            title = msoap.select('title')
            newtitle = title[0].getText().split('》')[0] + '》'
            sheet['A' + str(rownum)] = newtitle
            logging.info('[%d]:' % (rownum - 1) + newtitle)

            # 获取电影评分
            score = msoap.select('span strong')
            if len(score) > 0:
                sheet['B' + str(rownum)] = score[0].getText()
            else:
                sheet['B' + str(rownum)] = '0.0'

            # 获取下载链接,有多个下载地址时只取第一个
            mlist1 = msoap.select('table tbody tr td a')
            mlist2 = msoap.select('table tbody tr td font a')

            # print(str(len(mlist1)) + '\n')
            if len(mlist1) > 0:
                mlist = mlist1
            else:
                mlist = mlist2

            # print(mlist[0].get('href'))
            if len(mlist) > 0:
                sheet['C' + str(rownum)] = mlist[0].get('href')
            rownum += 1

resFile.save('movfy_20191110.xlsx')'''