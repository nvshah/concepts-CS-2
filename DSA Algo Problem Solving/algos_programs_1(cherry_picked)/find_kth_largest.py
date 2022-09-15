import heapq as hp
from typing import List


def findKthLargest(nums: List[int], k: int) -> int:
    hp.heapify(nums)
    for _ in range(len(nums) - k):
        hp.heappop(nums)
    return nums[0]


def findKthLargest2(nums: List[int], k: int) -> int:
    nums.sort()
    return nums[-k]


def findKthLargest3(nums: List[int], k: int) -> int:
    return hp.nlargest(k, nums)[-1]
