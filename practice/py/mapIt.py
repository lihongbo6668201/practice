#! /usr/bin/python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser, sys

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
#else:
    # Get address from clipboard.
#    address = clipboard.paste()

webbrowser.open('https://www.baidu.com/s?wd=' + address)
#webbrowser.open('http://caipiao.163.com/award/ssq/2018001.html')
#webbrowser.open('http://caipiao.163.com/award/ssq/2018002.html')
