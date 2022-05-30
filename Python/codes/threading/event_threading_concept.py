import threading as thr

event = thr.Event()  

def task1():
    print('Waitinf for the Event to be triggered...\n')
    event.wait()
    print('After Event is triggered in task1 performing its own task...')

t = thr.Thread(target=task1)

t.start()  #this thread is performing task1 which is waiting for some event `event` to be triggered

i = input('Do you want event to be triggered (y/n) :')
if i.lower() == 'y' :
    event.set()