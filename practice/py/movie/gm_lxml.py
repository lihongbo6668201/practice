#! python3
# getmov.py - Get movie downlinks from www.dy2018.com

from lxml import etree
import requests, bs4, webbrowser, logging, openpyxl

# 设置日志
logging.disable(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# 主页面爬取
logging.info('1')
res = requests.get("https://www.dy2018.com/html/bikan/")
res.raise_for_status()
# soap = bs4.BeautifulSoup( res.text.encode('iso-8859-1'), "html.parser" )
logging.info('2')
etest = etree.HTML(res.text.encode('iso-8859-1'))
# slist = soap.select( 'td b a' )
logging.info('3')
slist = etest.xpath(u'//td/b/a[@href=".*.html"]')

print(slist[0].text)
print(slist[1].text)
print(slist[2].text)
print(slist[3].text)


'''# 将爬取结果写入excel中
resFile = openpyxl.Workbook()
sheet = resFile.get_active_sheet()
sheet.title = "movie list"

sheet['A1'] = "电影名称"
sheet['B1'] = "电影评分"
sheet['C1'] = "下载地址"
rownum = 2

#循环处理单个子页面
for i in range( len( slist ) ):
    if "dyzz" in slist[i].get('href'):
        continue
    else:
        mhtml = "https://www.dy2018.com" + slist[i].get('href')
        mres  = requests.get( mhtml )
        mres.raise_for_status()
        msoap = bs4.BeautifulSoup( mres.text.encode('iso-8859-1').decode('gbk'), "html.parser" )

        #获取电影名称
        title = msoap.select('title')
        sheet['A'+str(rownum)] = title[0].getText()
        logging.info( title[0].getText() )

        #获取电影评分
        score = msoap.select('span strong')
        sheet['B'+str(rownum)] = score[0].getText()
        logging.info( score[0].getText() )

        #获取下载链接,有多个下载地址时只取第一个
        mlist = msoap.select( 'table tbody tr td a' )
        sheet['C'+str(rownum)] = mlist[0].get('href')
        rownum += 1
    
resFile.save('mov.xlsx')
'''
