
'''
Remember <--

For n digits number we need log10(n) times to boil down to 0 (ie 1 digits)

IMPL :- 3 steps
'''

def sumOfNumbers(n):
    ''' For positive integer numbers {n} only 
        TC := log10(n)
    '''
    # 1. Unintentional Case - the constraint
    assert n>=0 and isinstance(n, int), "Number has to be +ve integer only !"
    # 2. Base case
    if n == 0: return 0  
    # 3. Recursive Case
    q, r = divmod(n, 10)
    return r + sumOfNumbers(q)  

if __name__ == '__main__':
    n = -120
    a = sumOfNumbers(n)
    print(a)
