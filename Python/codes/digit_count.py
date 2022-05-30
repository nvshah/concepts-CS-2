from math import log10

def digit_count_1(n):
    '''
        Computer don't represent floating point number in accurate way
    '''
    if n == 0 : return 1
    tn = -n if n < 0 else n
    return log10(tn) + 1

def digit_count_2(n):
    '''
       plain logic of above approach 
    '''
    tn = abs(n)  # -n if n < 0 else n
    cntr = 1
    while tn >= 10**cntr:
        cntr += 1
    return cntr 



n = 9999999999999999997
print(len(str(n)))     # 19
print(digit_count_1(n))  # 20, but actual it was 19 ?? -> just because floating point val are not accurately handled by computer system
print(digit_count_2(n)) # 19


