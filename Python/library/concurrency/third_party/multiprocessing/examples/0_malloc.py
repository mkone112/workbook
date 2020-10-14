from multiprocessing import Process
import os, time, datetime, random, tracemalloc

# number of child processes to spawn
PROC_NUM = 4
# maximum delay in seconds
MAX_DELAY = 6

tracemalloc.start()


def status():
    return (
        f'Time: {datetime.datetime.now()}\t'
        f'Malloc, Peak: {tracemalloc.get_traced_memory()}'
    )


def child(num):
    delay = random.randrange(MAX_DELAY)
    print(
        f'{status()}\t\tProcess {num}, PID: {os.getpid()}, Delay: {delay}'
        f'seconds...'
    )
    time.sleep(delay)
    print(f'{status()}\t\tProcess {num}: Done.')


if __name__ == '__main__':
    print(f'Parent PID: {os.getpid()}')
    for i in range(PROC_NUM):
        proc = Process(target=child, args=(i,))
        proc.start()