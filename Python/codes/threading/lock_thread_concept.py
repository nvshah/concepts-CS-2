import threading
import time

x = 1000

lock = threading.Lock()

def double():
    global x, lock 
    lock.acquire()
    while x < 2000:
        print(x)
        time.sleep(2)
    print('Over double-----')

def halve():
    global x 
    lock.acquire()
    while x > 1:
        x /= 2
        print(x)
        time.sleep(1)
    print('Over halve-----')

t1 = threading.Thread(target=double)
t2 = threading.Thread(target=halve)

t2.start()
t1.start()

