# Usecase Generator (Bidrectional Pipline) Communication
from collections import deque

def worker(f):
    ''' apply f() to all tasks given to this worker at Run time '''
    tasks = deque()
    val = None
    while True:
        batch = yield val
        val = None
        if batch is not None:
            tasks.extend(batch)
        elif tasks:
            args = tasks.popleft()
            val = f(*args)

def quiet_worker(f):
    ''' Example of using Bidirectional Flow'''
    while True:
        w = worker    # getting from caller to worker
        try:
            yield from w  # sending from worker to caller
        except Exception as ex:
            print(f'ignoring {ex.__class__.__name__}'

def example_worker():
    w = worker(str)
    w.send(None)
    w.send([(0,), (1,), (2,)]
    print(next(w))
    print(next(w))
    print(next(w))

