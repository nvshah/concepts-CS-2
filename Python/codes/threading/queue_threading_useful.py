import queue

#FIFO
fifo_q = queue.Queue()
#LIFO
lifo_q = queue.LifoQueue()
#priority Queue
priority_q = queue.PriorityQueue()

nums_1 = [10, 20, 30]

#Multiple threads no problem just take next element one at a time using Queue
 
for n in nums_1:
    fifo_q.put(n)
    lifo_q.put(n)
    priority_q.put((30-n, n))

for i in range(3):
    print("Fifo Q", fifo_q.get())
    print("Lifo Q", lifo_q.get())

while not priority_q.empty():
    print("Priority Q", priority_q.get())

