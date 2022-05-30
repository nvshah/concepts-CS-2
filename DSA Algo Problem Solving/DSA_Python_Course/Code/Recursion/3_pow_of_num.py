
'''
Remember <--

X^a * X^b = X^(a+b)
|
-> X^n = X * X^(n-1)

IMPL :- 3 steps
'''

def power(base, exp):
    ''' calculate the power of num {base} exponentially 
        TC := O(exp) 
    '''
    # 1. Unintentional Case - the constraint
    # assert int(exp) == exp, "Number must be integer only!"
    assert isinstance(exp, int), "Number must be integer only!"
    isNeg = exp < 0  # track if exp is negative or not

    # 2. Nested Fun to suffice needs (custom)
    def rec(n, e):
        # 2. Base case
        if e == 0: return 1  
        if e == 1: return base
        # 3. Recursive Case
        return n * power(n, e-1)

    # 3. Trigger
    res = rec(base, abs(exp))

    # 4. Custom Handling for -ve {exp}
    return 1/res if isNeg else res


if __name__ == '__main__':
    a = power(2, -1)  # 0.5
    print(a)
