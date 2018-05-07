import urllib.parse

par = urllib.parse.urlparse('http://scimg.jb51.net/allimg/160707/103-160FG62200527.jpg')
if par.scheme:
    print(1)
    print(par.scheme + '://' + par.netloc)
else:
    print(2)
    print(par.netloc)
