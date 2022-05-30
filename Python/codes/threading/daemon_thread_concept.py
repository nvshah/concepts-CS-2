import threading as thr
import time 
import os, sys

#globals
TXT = ""
FILE = "sample.txt"

def readfile():
    global TXT, FILE 
    while True:
        with open(os.path.join(sys.path[0], FILE), "r") as F:
            TXT = F.readline()
        time.sleep(3)

def printTxt():
    for _ in range(30):
        print(TXT)
        time.sleep(1)

if __name__ == '__main__':
    print(sys.path)
    #t1 = thr.Thread(target=readfile, daemon=True)
    #t2 = thr.Thread(target=printTxt)

    #t1.start()
    #t2.start()

