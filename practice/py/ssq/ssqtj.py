#! /usr/bin/python3

import os
import bs4
import openpyxl
import requests
import logging

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

# 表格初始化
for idx in range(1, 34):
    sheet['A' + str(idx + 1)] = idx
    sheet['B' + str(idx + 1)] = 0
    if idx < 17:
        sheet['C' + str(idx + 1)] = idx
        sheet['D' + str(idx + 1)] = 0

# 循环下载文件
'''for int_idx in range(int_id, 2018030):
    # http://kaijiang.500.com/ssq.shtml
    # http://kaijiang.500.com/shtml/ssq/19008.shtml
    res = requests.get('http://caipiao.163.com/award/ssq/%d.html' % int_idx)
    res.raise_for_status()
    outFile = open(path + '\\' + str(int_idx)+'.txt', 'w+')
    outFile.write(res.text)
    outFile.close()
    print(str(int_idx) + '.txt下载完成')'''

#rownum = 2

resFile.save(path + '\\' + 'movfy_20191110.xlsx')

# 主页面爬取
res = requests.get("http://kaijiang.500.com/ssq.shtml")
res.raise_for_status()

# 解析所有分页列表
soap = bs4.BeautifulSoup(res.text.encode('iso-8859-1'), "html.parser")
sfy = soap.select('span div a')
print('共' + str(len(sfy)) + '期' )

# 循环所有分页
# for idx in range(len(sfy)):
for idx in range(10):
    suburl = sfy[idx].get('href')
    logging.info(suburl)
    subres = requests.get(suburl)
    subres.raise_for_status()

    # 解析子页面
    subsoap = bs4.BeautifulSoup(subres.text.encode('iso-8859-1'), "html.parser")
    sublist = subsoap.select('tr td div ul li')

    # 解析红蓝号
    print("第%s" % sfy[idx].getText() + "期，红号：", end="")
    for subidx in range(6):
        # 红号
        red_no = sublist[subidx].getText()
        print(red_no + " ", end="")

    # 蓝号
    blue_no = sublist[6].getText()
    print("蓝号：", blue_no)

    ''''# 循环处理单个子页面
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
