def countdown(start=10):
    def run():
        nonlocal start 
        start -= 1
        return start
    return run 

takeoff = countdown(5)

for v in iter(takeoff, 1):
    print(v)