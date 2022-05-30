import sys

# 1 generators to save memory --------

l = [i for i in range(100)]
print(sum(l))
print(sys.getsizeof(l), 'bytes')  # 920 bytes

g = (i for i in range(100))
print(sum(l))
print(sys.getsizeof(g), 'bytes')  # 112 bytes

# 2 dict with default val ---------

d = {1: '1', 2: '2'}

d.setdefault(3, 0)
print(d.get(4, -1))  # -1
print(d[3])         # 0

# 3 Concat with .join() --------

# Bad !  (As String is immutable & every time GC & new string is created)

sl = ["The", "Fool", "Person"]
st = ""
for s in sl:
    st += s 

# good Way 
st = " ".join(sl)
