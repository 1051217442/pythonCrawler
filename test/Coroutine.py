import asyncio


class coroutineTest(object):

    def __init__(self):
        pass

    async def start(self):
        print('start running')
        r = await asyncio.sleep(1)  ##模拟io操作
        print('start endding', r)


c = coroutineTest()
# 获取EventLoop:
loop = asyncio.get_event_loop()
task = [c.start(), c.start()]
# 执行coroutine
loop.run_until_complete(asyncio.wait(task))
loop.close()
