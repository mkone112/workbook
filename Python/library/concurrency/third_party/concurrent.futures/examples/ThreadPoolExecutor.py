from concurrent.futures import ThreadPoolExecutor
from time import sleep


def return_after_5_secs(msg):
    sleep(5)
    return msg

pool = ThreadPoolExecutor(3)

future = pool.submit(return_after_5_secs, ('hello'))
print(future.done())
sleep(5)
print(future.done())
print(future.result())