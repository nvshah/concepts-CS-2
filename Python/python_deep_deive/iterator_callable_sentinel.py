def counter():
    i = 0
    def inc():
        nonlocal i
        i += 1
        return i 
    return inc