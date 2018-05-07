from gevent import monkey; monkey.patch_socket(); monkey.patch_all()
import gevent
import urllib.request


# def f(url):
#     print('GET: %s' % url)
#     resp = urllib.request.urlopen(url)
#     data = resp.read()
#     print('%d bytes received from %s.' % (len(data), url))
#
#
# gevent.joinall([
#         gevent.spawn(f, 'http://www.python.org/'),
#         gevent.spawn(f, 'http://www.yahoo.com/'),
#         gevent.spawn(f, 'http://github.com/'),
# ])


# 测试协程是否对局部变量有影响 结果-----没有，原因，协程也只有一个线程来运行的
def f(n):
    num = 0
    for i in range(n):
        num += i
        print(gevent.getcurrent(), i)
    print('num= %s' % num)


g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
g1.join()
g2.join()
g3.join()
