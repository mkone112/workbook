import threading
import time
import random


def worker(number):
    sleep = random.randrange(1, 10)
    time.sleep(sleep)
    print(f"I'm Worker {number}, I slept for {sleep} seconds")


for i in range(5):
    thread = threading.Thread(target=worker, args=(i,))
    thread.start()

print("All Threads are queued, let's see when they finish!")