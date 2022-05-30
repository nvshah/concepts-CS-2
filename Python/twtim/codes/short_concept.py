# 1 Binary & Decimal ----

n = 23
b = bin(n)[2:]  # to discard 0b..
d = int(b, 2)
print(b, '<->' ,d)  # 10111 <-> 23