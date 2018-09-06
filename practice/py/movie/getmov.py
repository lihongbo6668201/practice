#! python3
# getmov.py - Get movie downlinks from www.dy2018.com

import requests, bs4, webbrowser, logging

#设置日志
logging.disable(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

#主页面爬取
res = requests.get("https://www.dy2018.com/html/bikan/")
res.raise_for_status()
soap = bs4.BeautifulSoup( res.text, "html.parser" )
slist = soap.select( 'td b a' )

#循环处理单个子页面
for i in range( len( slist ) ):
    if "dyzz" in slist[i].get('href'):
        continue
    else:
        mhtml = "https://www.dy2018.com" + slist[i].get('href')
        mres  = requests.get( mhtml )
        mres.raise_for_status()
        msoap = bs4.BeautifulSoup( mres.text, "html.parser" )
        mlist = msoap.select( 'table tbody tr td a' )

        #取名称和评分
        title = msoap.select( 'title')
        logging.info( title[0].getText() )

        #获取下载链接
        for j in range( len( mlist ) ):
            logging.info( '[%d]' % j + mlist[j].get('href'))
        
    
#plist = soap.select()
