
from math import ceil

'''
At Odd Places there will be -ve Vals 
So whilst reducing n everytime by dividing it with 2(or base) Here 
Alternate time we will reduce whereas alternate time it will icrease it 
'''


def decimalToBase(n, b):
    '''
        Convert decimal num {n} to base {b}
    '''
    if n == 0: return "0"
    res = []
    if b < 0:   # -ve Base
        while n:
            n, r = ceil(n/b), abs(n%b)
            res.append(str(r))
    else:       # +ve base
        while n:
            n, r = divmod(n, b)
            res.append(str(r))
    return ''.join(reversed(res))

if __name__ == '__main__':
    n = 6
    ans = decimalToBase(n, 2)
    print(ans)  # 110
    ans = decimalToBase(n, -2)
    print(ans)  # 11010

