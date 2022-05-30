import math

def find_floor(arr, t):
    '''return the index of element (assuming index start from 1)'''
    s, e = 0, len(arr)-1
    while s <= e:
        m = s + (e - s) //2
        if t > arr[m]:
            s = m + 1
        elif t < arr[m]:
            e = m - 1
        else:
            return m + 1
    return e + 1

def speculate_initial_val(n):
    '''
    The Rule of Twos and Sevens chooses an initial guess from among the candidates {2, 7, 20, 70, 200, 700, ...}
    '''
    zeros = pow(10, len(str(n)) // 2)
    l, u = 2 * zeros, 7 * zeros
    l_squared, u_squared = 4 * zeros, 49 * zeros
    m = l_squared + (u_squared-l_squared) // 2  # closeness|proximity decision
    i = l if n < m else u # initial val
    return i

def babylonian_sqrt(num):
    '''
    Find the math.isqrt() via babylonian method of approximation

    BABYLONIAN LOGIC :- 
    ref https://blogs.sas.com/content/iml/2016/05/16/babylonian-square-roots.html

    intital values :- 
        {2, 7, 20, 70, 200, 700 }

    NOTE this is similar to math.isqrt() in python
        import math
        print(math.isqrt(10)) # 3
    '''
    if num < 225:
        sqs = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]
        return find_floor(sqs, num)
    i = speculate_initial_val(num)
    #print('Initial : ', i)
    # find the initial val
    while True:
        #b = round((i + num / i) / 2, decimal_precision)
        #b = floor((i + num / i) / 2)
        b = (i + num / i) / 2
        #print('-> ', b)
        if math.floor(i) == math.floor(b):
            return math.floor(i)
        else:
            i = b

def isqrt(n):
    '''
    math.isqrt() via Binary Search (an alternative to babylonian )

    Logic ->

    Let's consider
    number - n, divisor - d

    if d divides n into exact d parts then we can say that d is exact square root of n
    if d divides n into more than d parts so -> need to lower the divider
    if d divides n into less than d parts sp -> need to increase the divider
    '''
    s, e = 1, n
    while s <= e:
        m = s + (e-s) // 2
        q = n // m
        if m == q:
            # m divides n into exact d parts, i.e found exact square root
            return m
        elif q > m:
            # m divides n into more than m parts, i.e more parts than expected so increase the divider
            s = m+1
        else:
            # d divides n into less than d parts i.e less parts than expected so decrease the divider
            e = m-1
    return e