import datetime
import time


def current():
    return time.strftime('%Y-%m-%d %H:%M:%S')


def current(pattern='%Y-%m-%d %H:%M:%S'):
    # 按格式输出
    return time.strftime(pattern, time.localtime(time.time()))


def timecast(starttime):
    endtime = datetime.datetime.now()
    return (endtime-starttime).seconds


print(current())
print(timecast(datetime.datetime.now()))
