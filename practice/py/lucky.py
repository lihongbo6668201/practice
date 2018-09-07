#! python3
# lucky.py - Opens several Baidu search results.

import requests, sys, webbrowser, bs4, logging

print('Searching...') # display test while downloading the Baidu page
tfile = open('lihb.txt', 'w')
res = requests.get('https://www.sogou.com/web?query=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
tfile.write(res.text)
tfile.close()

#webbrowser.open('https://www.sogou.com/web?query=' + ''.join(sys.argv[1]))

# Retrieve top search result links.
testSoup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open a browser tab for each result.
linkElems = testSoup.select('h3 a')
numOpen = min(5, len(linkElems))
print(str(numOpen)+'\n')
#logging.debug(numOpen)
for i in range(numOpen):
    print(linkElems[i].get('href'))
    webbrowser.open('http://www.sogou.com' + linkElems[i].get('href'))

