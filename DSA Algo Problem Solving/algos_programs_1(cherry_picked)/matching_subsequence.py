# https://leetcode.com/problems/number-of-matching-subsequences/

from bisect import bisect
from collections import defaultdict
from typing import List


def isMatchingSubseq(s: str, t: str) -> int:
    ''' Check if t is sub sequence of s '''
    lookup = defaultdict(list)
    # char -> positions
    for i, c in enumerate(s):
        lookup[c].append(i)

    # prev := index in s till which characters are matched for t
    prev = -1
    for c in t:
        lst = lookup[c]
        # get the right next index to [prev] from [lst]
        i = bisect(lst, prev)
        # no index is found closest to [prev] on right side in [lst]
        if i == len(lst):
            break
        prev = lst[i]
    else:
        return True
    return False


s = "abcde"
t = "accd"

ans = isMatchingSubseq(s, t)
print(ans)
