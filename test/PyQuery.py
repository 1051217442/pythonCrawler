import json
import urllib
import re

from pyquery import PyQuery as pq

query = urllib.parse.quote("风景")
url = 'http://image.baidu.com/search/avatarjson?tn=resultjsonavatarnew&ie=utf-8&word=' + query + '&cg=girl&pn=1&rn=60&itg=0&z=0&fr=&width=&height=&lm=-1&ic=0&s=0&st=-1&gsm=1e0000001e'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = urllib.request.Request(url=url, headers=headers)
page = urllib.request.urlopen(req)
rsp = page.read().decode('utf-8')

q = re.search(u'.imgs+',rsp)
print(q)
for im in q:
    print(im)
# pageMap = json.loads(rsp)
# for img in pageMap['imgs']:
#     print(str(img['objURL'])+"\n")