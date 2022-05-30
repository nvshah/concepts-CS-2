# https://leetcode.com/problems/find-k-closest-elements/

from typing import List

'''
TASK: 
Numbers in arr are sorted already
Given number {x}, You need to find {k} closest element from that {arr}
'''

# SEMI BEST WAY (LAMUTO)
def findClosestElements2(arr: List[int], k: int, x: int) -> List[int]:
    ''' IDea : Lamuto Quick Sort Pivot Find Logic '''
    l, r = 0, len(arr)-1

    while (r - l + 1) != k:
        dl = abs(arr[l] - x)
        dr = abs(arr[r] - x)

        if dl <= dr:
            r -= 1
        else:
            l += 1
        
    return arr[l:r+1]

# BEST WAY (BINARY SEARCH)
def findClosestElements3(arr: List[int], k: int, x: int) -> List[int]:
    ''' IDea : Find Window via Binary Search '''
    # mid val will point the start of window & window needs length = k so hi is last kth elem
    lo, hi = 0, len(arr)-k

    # Here in Binary Search it will always converge entirely ie log(n)
    # Thus we want lo & hi to point to same num at the end of this binary search & that number will be start index of (ideal) window
    while lo < hi:
        mi = (lo + hi) // 2  
        # e is the next element outside the window (on right side)
        s, e = mi, mi+k     # start & end of window (start including)
        if x - arr[s] > arr[e] - x:
            # {s} is not closest compare to {e}
            # so include {e} in window & exclude {s}  
            # thus excluding all left side of curr window [s, e)  ie all elem <= {s}
            lo = mi + 1
        else:
            # {mi} can be equally or less closest  
            # thus neglecting all right side of current window [s, e)  ie all elem >= {e}
            hi = mi
    
    # Now lo = hi & thus this will be start idx of window
    return arr[lo: lo+k]