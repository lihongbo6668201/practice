#! python3
# getmov.py - Get movie downlinks from www.dy2018.com

import requests, bs4, logging, openpyxl, time

#设置日志
logging.disable(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

#主页面爬取
res = requests.get("https://www.dy2018.com/html/gndy/dyzz/index.html")
res.raise_for_status()

#将爬取结果写入excel中
resFile = openpyxl.Workbook()
sheet = resFile.active
sheet.title = "movie list"

#excel标题栏
sheet['A1'] = "电影名称"
sheet['B1'] = "电影评分"
sheet['C1'] = "下载地址"
rownum = 2

#解析所有分页列表
soap = bs4.BeautifulSoup(res.text.encode('iso-8859-1'), "html.parser")
sfy = soap.select('select option')

#循环所有分页
for idx in range(len(sfy)):
    suburl = "https://www.dy2018.com" + sfy[idx].get('value')
    logging.info(suburl)
    subres = requests.get(suburl)
    subres.raise_for_status()

    #解析子页面
    subsoap = bs4.BeautifulSoup( subres.text.encode('iso-8859-1'), "html.parser")
    sublist = subsoap.select( 'td b a' )

    #循环处理单个子页面
    #for i in range( len( sublist ) ):
    for i in range(9):

        if "dyzz" in sublist[i].get('href') or "oumeitv" in sublist[i].get('href'):
            continue
        else:
            #获取详细页面
            mhtml = "https://www.dy2018.com" + sublist[i].get('href')
            #logging.info(mhtml)
            mres  = requests.get( mhtml )
            mres.raise_for_status()
            msoap = bs4.BeautifulSoup( mres.text.encode('iso-8859-1').decode('gbk'), "html.parser" )

            #获取电影名称
            title = msoap.select('title')
            newtitle = title[0].getText().split('》')[0] + '》'
            sheet['A'+str(rownum)] = newtitle
            logging.info( '[%d]:' % (rownum-1) + newtitle )

            #获取电影评分
            score = msoap.select('span strong')
            if len( score ) > 0:
                sheet['B'+str(rownum)] = score[0].getText()
            else:
                sheet['B'+str(rownum)] = '0.0'

            #获取下载链接,有多个下载地址时只取第一个
            mlist1 = msoap.select( 'table tbody tr td a' )
            mlist2 = msoap.select( 'table tbody tr td font a' )

            #print(str(len(mlist1)) + '\n')
            if len(mlist1) > 0:
                mlist = mlist1
            else:
                mlist = mlist2

            #print(mlist[0].get('href'))
            if len(mlist) > 0:
                sheet['C'+str(rownum)] = mlist[0].get('href')
            rownum += 1
    
resFile.save('gmall_' + time.strftime('%Y%m%d', time.localtime()) + '.xlsx')
