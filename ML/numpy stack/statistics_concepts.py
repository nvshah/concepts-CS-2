import numpy as np 

# 1
# Standard Deviation Range
temp_sensor = np.array(
[ 18, 22, 22, 18 ]) 
mean = np.mean(temp_sensor)
std = np.std(temp_sensor)
print(str(int(mean - std)) + "-" + str(int(mean + std)))

# 2
# Sensor values
values = np.array([815, 767, 554, 141, 605, 346])
indices = np.nonzero((values < 200) | (values > 800))
print(indices[0][1])