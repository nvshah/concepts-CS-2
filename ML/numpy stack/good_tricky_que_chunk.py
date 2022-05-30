import numpy as np

# Memory allocation:
# '1' means allocated, '0' means free
memory = np.array([0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0])

# start and end indices of
# contiguous memory allocations
diff = np.diff(memory)
starts = np.nonzero(diff == 1)[0] + 1
ends = np.nonzero(diff == -1)[0]
sizes = ends - starts
indices = np.argsort(sizes)
for i in range(len(sizes)):
    print((starts[indices[i]], ends[indices[i]], sizes[indices[i]],),)

