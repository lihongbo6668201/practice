# -*- coding:utf-8 -*-
import re
import requests

def dowmloadPic(html, keyword):
    #pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
    print(len(pic_url))
    i = 1
    print('找到关键词:' + keyword + '的图片，现在开始下载图片...')
    for each in pic_url:
        print('正在下载第' + str(i) + '张图片，图片地址:' + str(each))
        try:
            pic = requests.get(each, timeout=10)
        except requests.exceptions.ConnectionError:
            print('【错误】当前图片无法下载')
            continue

        #dir = '../images/' + keyword + '_' + str(i) + '.jpg'
        dir = 'C:\\images\\' + keyword + '_' + str(i) + '.jpg'
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
        i += 1

if __name__ == '__main__':
    word = input("Input key word: ")
    #url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&ct=201326592&v=flip'
    url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1573570681020_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word=' + word
    result = requests.get(url)
    #print(result.text)
    dowmloadPic(result.text, word)