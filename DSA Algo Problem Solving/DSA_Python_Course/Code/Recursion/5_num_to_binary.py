
'''
Remember <--

Traditional Way :- divide by 2 until get 1

Eg 10 -> binary
    10/2  5   0
    5/2   2   1
    2/2   1   0
    1/2   0   1
              => 1010   // To get ans read from backside to top

    1010 := 1*10^3 + 0*10^2 + 1*10 + 0*1
'''

def toBinary(n):
    ''' convert decimal {n}  to its binary (ie base 2) form
        returns binary number 
        TC := O(log_2(n))
    '''
    # 1. Unintentional Case - the constraint
    assert isinstance(n, int), "Numbers must be integer only!"
    # 2. Base case
    if n == 0: return 0   # 0 adds no value to number
    # 3. Recursive Case
    return (n % 2) + (10 * toBinary(n//2))


if __name__ == '__main__':
    a = toBinary(12)
    print(a)
