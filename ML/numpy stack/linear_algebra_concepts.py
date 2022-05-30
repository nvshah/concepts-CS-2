import numpy as np

# 1. 
# Distance between Two points in 3D space
a = np.array([5, -3, 2])
b = np.array([1, 0, 2])
c = b - a
vec_len = np.sqrt(sum(c ** 2))
print(int(vec_len))

# 2. 
# Cross Product between 2 vectors
# Two vectors in 3D space
a = np.array([5, -3, 2])
b = np.array([1, 0, 2])
c = np.cross(a, b)
scalar_prod = np.dot(a, c)
# Since vector c was computed to be orthogonal to vector a, the scalar product is 0.
print(scalar_prod)  # 0

# 3 
# Weighted Avg along axis
# daily stock prices
# [morning, midday, evening]
solar_x = np.array([[2, 3, 4], [2, 2, 5]])  # today  # yesterday
# midday - weighted average
# axis = 0 -> row & weeights are multiplied to each row
print(np.average(solar_x, axis=0, weights=[3 / 4, 1 / 4])[1])

#4. 
# variance Goals in five matches
goals_croatia = np.array( [0,2,2,0,2])
goals_france = np.array( [1,0,1,1,0])
c = np.var(goals_croatia) 
f = np.var(goals_france) 
print(c>f)

# 5
# stock prices (3x per day) 
# [morning, midday, evening] 
APPLE = np.array(
[[50,60,55], # day 1 
[60,60,65]]) # day 2
# midday variance
y = np.var(APPLE, axis=0)[1] 
print(int(y))
