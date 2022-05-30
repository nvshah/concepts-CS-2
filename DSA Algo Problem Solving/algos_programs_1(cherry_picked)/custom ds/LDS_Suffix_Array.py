''' SUFFIX ARRAY '''

import logging
import operator as op
from functools import partial

logging.basicConfig(level=logging.DEBUG)

def commonPrefixSize(s1, s2, start=0): 
    ''' Find common prefix length from starting index between 2 string'''
    cLen = min(len(s1), len(s2))  # exhausting length
    s = 0  
    if start < cLen:  
        for c1, c2 in zip(s1[start:], s2[start:]):   # count common starting characters
            if c1 != c2:
                return s 
            s += 1
    return s

def suffix_array(s):
    size = len(s)
    return sorted(range(size), key=lambda i: s[i:])

def rank_array(sa):
    size = len(sa)
    ra = [0]*size   
    for r, i in enumerate(sa):
        ra[i] = r
    return ra 

def lcp_kasai_algo(s, sa, ra):
    size = len(s)
    # 3. Kasai Algo to Find LCP array
    lcp = [0]*size  # Longest Common Prefix Array
    skip = 0  # number of prefix going to be common for next comparision (so we can skip those characters in next comparision)
    for i in range(size):
        rank = ra[i]
        if rank == 0: continue 
        p = sa[rank-1] # find prev suffix index
        curr = s[i:]
        prev = s[p:]
        lcp[rank] = common = skip + commonPrefixSize(curr, prev, skip)
        skip = max(0, common - 1)
    return lcp

# Longest Duplicate(Repeating) Substring
def lrs(s):
    '''Longest Repeating SubStrings (Longest Duplicating (Contiguous) Substring) LDS'''
    # 1. Suffix Array
    sa = suffix_array(s)
    logging.info(f'{sa=}')
    # 2. Rank Array
    ra = rank_array(sa)
    # 3. Lcp Array 
    lcp = lcp_kasai_algo(s, sa, ra)
    logging.info(f'{lcp=}')
    # 4. LRS length = max value in LCP array = max(lcp)
    lrs_len = max(lcp)  
    #mEq = partial(op.eq, lrs_len)
    ranks = [i for i in range(len(s)) if lcp[i] == lrs_len]
    lds = set()   # longest repeating substring = prefix of length {max(lcp)} of suffix corresp to {sa[rank]}
    for r in ranks:
        l = sa[r] # lower bound = original staring index of suffix
        u = l + lrs_len # upper bound = LRS length = max(lcp)
        lds.add(s[l:u])

    # NOTE : There can be more than 1 LDS possible answer
    return lds 

    # 4. LRS length = max value in LCP array = max(lcp)
    # rank = max(range(len(s)), key=lcp.__getitem__)  # (argmax to get rank)
    # u = lcp[rank]  # upper bound = LRS length = max(lcp)
    # l = sa[rank]   
    # lds = s[l: l+u]  # longest repeating substring = prefix of length {max(lcp)} of suffix corresp to {sa[rank]}

if __name__ == '__main__':
    s = 'bananaban'
    s = "abcd"
    s = 'banana'
    print(f'lrs = {lrs(s)}')