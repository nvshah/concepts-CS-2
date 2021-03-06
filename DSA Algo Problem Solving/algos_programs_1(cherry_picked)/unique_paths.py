# https://leetcode.com/problems/unique-paths/

# ref Math Work : 
# https://mathigon.org/task/paths-on-a-grid

'''
Unique Path = (m+n-2)C(m-1)

You can think This matrix as Pascal Triangle
'''

import math

def uniquePaths(m: int, n: int) -> int:
    # last row & last column going to have all 1 
    prevRow = [1] * n 

    for _ in range(m-1): # Skipping last row
        currRow = [1] * n
        for j in range(n-2, -1, -1): # starting from last second element (as last elem always going to be 1)
            right, bottom = currRow[j+1], prevRow[j]
            currRow[j] = right + bottom
        prevRow = currRow
    
    return prevRow[0]

def uniquePaths2(m: int, n: int) -> int:
    return math.comb(m+n-2, m-1)

