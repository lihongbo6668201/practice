#! /usr/bin/python3
#import webbrowser
#webbrowser.open('http://inventwithpython.com/')
#webbrowser.open('https://www.google.com/maps/place/Bank+of+Gansu/')

import requests
id = 2018001


for id in range(id,2018030):
    res = requests.get('http://caipiao.163.com/award/ssq/%d.html' % id)
    res.raise_for_status()
    outFile = open('ssq'+str(id)+'.txt', 'w+')
    outFile.write(res.text)
    outFile.close()
#if res.status_code == requests.codes.ok:
#    print('True')

#print(res.text)
#print(res.text[:250])
