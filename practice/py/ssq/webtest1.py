#! /usr/bin/python3
#import webbrowser
#webbrowser.open('http://inventwithpython.com/')
#webbrowser.open('https://www.google.com/maps/place/Bank+of+Gansu/')

import requests, bs4, logging

#logging.disable(logging.INFO)
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
id = 2018001

resultFile = open('result.txt', 'w')

for id in range(id, 2018150 ):

    res = requests.get('http://caipiao.163.com/award/ssq/%d.html' % id)
    #res.raise_for_status()
    if ( res.status_code != requests.codes.ok ):
        continue

    testSoup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = testSoup.select('#zj_area')

    #logging.debug(str(elems[0]))
    logging.info(str(id) + ' : ' + elems[0].getText( ))
    resultFile.write( str(id) + '期: ' + elems[0].getText(' ').replace("\n", "") + '\n')

resultFile.close()
#outFile = open('ssq'+str(id)+'.txt', 'w+')
#outFile.write(res.text)
#outFile.close()
#if res.status_code == requests.codes.ok:
#    print('True')

#print(res.text)
#print(res.text[:250])
