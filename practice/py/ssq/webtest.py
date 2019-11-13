#! /usr/bin/python3

import os
import requests

int_id = 2018001

# 创建目录
path = r'C:\双色球'
if not os.path.exists(path):
    os.makedirs(path)


# 循环下载文件
for int_idx in range(int_id, 2018030):
    res = requests.get('http://caipiao.163.com/award/ssq/%d.html' % int_idx)
    res.raise_for_status()
    outFile = open(path + '\\' + str(int_idx)+'.txt', 'w+')
    outFile.write(res.text)
    outFile.close()
    print(str(int_idx) + '.txt下载完成')
