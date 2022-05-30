import random

random.seed(0)

for i in range(1, 8):
    print(random.randint(1, 5))
    
print('-------')

random.seed(0)
for j in range(1, 5):
    print(random.randint(1, 5))

random_num = iter(lambda : random.randint(1, 5), 1)
random.seed(0)

print('-------')

for n in random_num:
    print(n) 
    


