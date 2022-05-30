from typing import List

def binary_search_plain(arr, target, start=0, end=-1):
    ''' Binary Search for Sorted Array using Iterator Approach '''
    end = end if end != -1 else len(arr) - 1
    while start <= end:
        mid = start + ((end - start) // 2)
        if target > arr[mid]:
            start = mid + 1
        elif target < arr[mid]:
            end = mid - 1
        else:
            return mid
    return -1

def find_pivot_in_rotated_sorted_array(nums: List[int]) -> int:
    '''
    Find the index of maximum number if array is rotated atleast
    NOTE - pivot is largest elem because there can be only chance that
           largest elem,the following element will always be smallest
    (Assuming Unique elements in array)
    :param nums: list of rotated sorted array
    :return: index of maximum number if array is rotated (i.e except first & last element index)
    '''
    s, e = 0, len(nums) - 1
    while s <= e:
        m = s + (e - s) // 2
        if m < e and nums[m] > nums[m + 1]:
            return m  # pivot found i.e Peak -> smallest
        elif m > s and nums[m - 1] > nums[m]:
            return m - 1  # pivot found i.e Peak -> smallest
        elif nums[s] < nums[m]:
            # increasing left part so max element will lie in right part
            s = m + 1
        else:
            # nums[s] > nums[m]
            # peak can be in left part (as all elem in right part is smaller than left part)
            e = m - 1
    return -1

def find_pivot_in_rotated_sorted_array_with_duplicates(nums: List[int]) -> int:
    '''
    Find the index of maximum number if array is rotated atleast
    NOTE - pivot is largest elem because there can be only chance that
           largest elem,the following element will always be smallest
    (Array may include duplicate elements in array)
    :param nums: list of rotated sorted array
    :return: index of maximum number if array is rotated (i.e except first & last element index)

    1) num[s] == nums[m] == nums[e]
        in which case we will ignore s & e items after pivot check
    2) When num[s] == nums[m]
       - It delineats that s -> m all elements are same so search in right (after considering first point)
    '''

    s, e = 0, len(nums) - 1
    while s <= e:
        m = s + (e - s) // 2
        if m < e and nums[m] > nums[m + 1]:
            return m  # pivot found i.e Peak -> smallest
        elif m > s and nums[m - 1] > nums[m]:
            return m - 1  # pivot found i.e Peak -> smallest
        elif nums[s] == nums[m] == nums[e]:
            # check and ignore start
            if s < e and nums[s] > nums[s + 1]:
                return s
            else:
                s += 1
            # check and ignore end
            if e > s and nums[e - 1] > nums[e]:
                return e - 1
            else:
                e -= 1
        elif nums[s] <= nums[m]:
            # increasing left part so max element will lie in right part
            # (here if s == m then also it means that s->m all are equal elements)
            s = m + 1
        else:
            # nums[s] > nums[m]
            # peak can be in left part (as all elem in right part is smaller than left part)
            e = m - 1
    return -1

def search_in_rotated_sorted_array(nums: List[int], target: int, unique=False) -> int:
    if unique:
        kingMaker = find_pivot_in_rotated_sorted_array(nums)
    else:
        kingMaker = find_pivot_in_rotated_sorted_array_with_duplicates(nums)
    # if kingMaker is found i.e we have found 2 asc sorted array
    if kingMaker == -1:
        # No rotation on nums
        binary_search_plain(nums, target)
    elif nums[kingMaker] == target:
        return kingMaker
    elif target < nums[0]:
        # search in right part of kingmaker (i.e lower values bunch)
        binary_search_plain(nums, target, kingMaker + 1)
    else:
        # search in left part of kingmaker (i.e higher values bunch)
        binary_search_plain(nums, target, 0, kingMaker)

def find_rotation_count_in_sorted_array(nums: List[int], unique=False) -> int:
    if unique:
        pivot_idx = find_pivot_in_rotated_sorted_array(nums)
    else:
        pivot_idx = find_pivot_in_rotated_sorted_array_with_duplicates(nums)
    return pivot_idx + 1

if __name__ == '__main__':
    arr = [4,5,6,1,2,3]
    #arr = [2,2,2,2,2,9,2]
    arr = [2,2,9,2,2,2,2,2,2]
    #pivot = find_pivot_in_rotated_sorted_array_with_duplicates(arr)
    #ans = search_in_rotated_sorted_array(arr, 1)

    rot_cnt = find_rotation_count_in_sorted_array(arr)

    print(rot_cnt)