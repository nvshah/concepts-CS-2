from typing import List, Tuple


def maxSubArray_ka(nums: List[int]) -> Tuple[List[int], int]:
    """
    Logic -> Kadane's Algorithm
    gist : start linear traverse from first element, & keep track of
           {current sum, max sum, start idx & end idx of subarray}
           If for any item, item > current sum(i.e including that item)
              then just reset ptrs for subarray from this item.

    @param nums -> array of numbers
    @return -> typle containing array as well as max sum value
    """
    ptr1 = 0
    ptr2 = 0
    curr_sum = nums[0]
    max_sum = nums[0]
    for i, n in enumerate(nums[1:], 1):
        curr_sum += n
        if curr_sum < n:  # case esp when -ve numbers arrives between 2 positive nums
            ptr1 = ptr2 = i
            curr_sum = max_sum = n
        elif curr_sum > max_sum:
            max_sum = curr_sum
            ptr2 = i

    return (nums[ptr1 : ptr2 + 1], max_sum)
