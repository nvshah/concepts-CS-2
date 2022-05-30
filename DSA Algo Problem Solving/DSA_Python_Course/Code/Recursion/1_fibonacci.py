
def fibo(n):
    #assert n >= 0 and int(n) == n
    assert n >= 0 and isinstance(n, int), 'Fibonacci number cannot be -ve nnumber or non-integer'

    if n in (0, 1):
        return n
    return fibo(n-1) + fibo(n-2)

print(fibo(4))