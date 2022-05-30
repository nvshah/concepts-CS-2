import math

# factorial using interators
def fact():
    i = 0

    def inner():
        nonlocal i
        r = math.factorial(i)
        i += 1
        return r
    return inner


i1 = fact()  #Infinite Iterator

i2 = iter(i1, math.factorial(5)) #finite Iterator

list(i2) #[1,1,2,6,24]
list(i2) #[]

