# generators_general_concept.py
import math

#It is generator factory
def factorials(n):
    for i in range(n):
        yield math.factorial(i)

fact_iter = factorials(5)

#Check if factorials is iterator

print('__iter__' in dir(fact_iter))  # True
print('__next__' in dir(fact_iter))  # True

for i in fact_iter:
    print(i)

#---------------------------
#2nd Eg

def f():
    print('First')
    yield 'Yeet'
    print('Second')
    yield 'Austere'
    print('Third')

fn = f()

type(fn)
print(iter(fn) is fn)

print(fn.__next__())
print(next(fn))


#---------------- return in generators

def fake():
    yield 1
    yield 2
    return 3
    yield 4

fo = fake()
next(fo) #1
next(fo) #2
next(fo) # StopIteration: 3
