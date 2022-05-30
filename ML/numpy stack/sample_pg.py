import numpy as np 

'''
sum(a) = np.sum(a, axis=0)
'''


a1 = np.array([[1,2,3], [4,5,6]])

a2 = np.array([[[1,2], [3,4]], [[5,6],[7,8]]])

print(sum(a1)) # will return numpy array
print(np.sum(a1))  # flatten & do sum

print(sum(a2))
print(np.sum(a2, axis=0)) 