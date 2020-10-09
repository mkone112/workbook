'''
Запуск 2x асинхронных циклов выводящих в консоль datetime
python 3.5+
'''
import asyncio
import datetime
import random


async def my_sleep_func():
    await asyncio.sleep(random.randint(0, 5))

#принимает eventloop
async def display_date(num, loop):
    end_time = loop.time() + 50.0
    while True:
        print('Loop: {} Time: {}'.format(num, datetime.datetime.now()))
        #завершается через 50 сек
        if (loop.time() + 1.0) >= end_time:
            break
        #цикл засыпает на 1-5 сек
        await my_sleep_func()


loop = asyncio.get_event_loop()

asyncio.ensure_future(display_date(1, loop))
asyncio.ensure_future(display_date(2, loop))

loop.run_forever()

'''
>>
    Loop: 1 Time: 2020-10-08 14:54:32.918372
    Loop: 2 Time: 2020-10-08 14:54:32.918372
    Loop: 1 Time: 2020-10-08 14:54:35.933920
    Loop: 2 Time: 2020-10-08 14:54:35.933920
    Loop: 2 Time: 2020-10-08 14:54:39.949505
    Loop: 1 Time: 2020-10-08 14:54:40.933864
    Loop: 2 Time: 2020-10-08 14:54:41.965072
    ...
'''