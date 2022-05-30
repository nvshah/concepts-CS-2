import threading
import time

semaphore = threading.BoundedSemaphore(value=5)

def srcAccess(thread_num):
    print(f"trying to access for {thread_num} <--")
    semaphore.acquire()
    print(f"access granted for {thread_num} !")
    time.sleep(10)
    print(f"releasing src for {thread_num} -->")
    semaphore.release()

for num in range(1, 8):
    t = threading.Thread(target=srcAccess, args=(num,))
    t.start()
    time.sleep(2)
