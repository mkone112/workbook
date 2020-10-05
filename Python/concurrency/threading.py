#код на первый взляд ЭКВ multipocessing
#жрет меньше mem чем multiprocessing, но по факту не exe параллельно(CPython)
#es:
    from threading import Thread
    import os, time, datetime, random, tracemalloc
    
    tracemalloc.start()
    # number of child threads to spawn
    NUM_THREADS = 4
    # maximum delay in seconds
    MAX_DELAY = 6
    
    
    def status():
        return (
            f'Time: {datetime.datetime.now().time()}'
            f'\t Malloc, Peak: {tracemalloc.get_traced_memory()}'
        )
    
    def child(num):
        delay = random.randrange(MAX_DELAY)
        print(
            f'{status()}\t\tProcess {num}, PID: {os.getpid()}, Delay: {delay}'
            f'seconds..'
        )
        time.sleep(delay)
        print(f"{status()}\t\tProcess {num}: Done.")
    
    
    if __name__ == '__main__':
        print(f'Parent PID: {os.getpid()}')
        for i in range(NUM_THREADS):
            thr = Thread(target=child, args=(i,))
            thr.start()