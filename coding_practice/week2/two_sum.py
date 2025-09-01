"""
Two Sum - LeetCode #1
Given an array nums and a target, return indices of the two numbers that add up to target.
Example: nums = [2,7,11,15], target = 9 → Output: [0,1]
"""

def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target-n], i]
        seen[n] = i

# Test
print(two_sum([2,7,11,15], 9))  
print(two_sum([3,2,4], 6))      

