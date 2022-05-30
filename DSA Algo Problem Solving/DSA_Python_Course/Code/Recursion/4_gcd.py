
'''
Remember <--

GCD of 2 nums is largest num that can divide both the numbers wholely

Also :- GCD of -ve nums = GCD of +ve nums

Eucledian Algo :
  gcd(a,0) := a     // {a} being divided by {0}
  gcd(a,b) = gcd(b, a mod b)  // {a} being divided by {b}
'''

def gcd(a, b):
    ''' calculate the gcd for 2 nums a, b
        TC := O(log_b(a))
    '''
    # 1. Unintentional Case - the constraint
    assert isinstance(a, int) and int(b) == b, "Numbers must be integer only!"
    # 1.1 Convert both to +ve (ie same sign) as `GCD of -ve nums = GCD of +ve nums`
    a, b = abs(a), abs(b)
    # 2. Base case
    if b == 0: return a   
    # 3. Recursive Case
    return gcd(b, a%b)


if __name__ == '__main__':
    a = gcd(48, 18)  # 6
    print(a)
