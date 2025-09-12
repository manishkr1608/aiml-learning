"""
Maximum Subarray – LeetCode #53
Find the contiguous subarray with the largest sum.
Example: [-2,1,-3,4,-1,2,1,-5,4] → 6 (subarray [4,-1,2,1])
"""

def max_subarray(nums):
    cur_sum = max_sum = nums[0]
    for n in nums[1:]:
        cur_sum = max(n, cur_sum + n)
        max_sum = max(max_sum, cur_sum)
    return max_sum

# Tests
print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
print(max_subarray([1]))  # 1
print(max_subarray([5,4,-1,7,8]))  # 23

