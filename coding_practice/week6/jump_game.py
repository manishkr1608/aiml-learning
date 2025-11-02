
"""
Jump Game - LeetCode #55
Greedy approach: always keep track of the farthest reachable index.
"""
def canJump(nums):
    reach = 0
    for i, step in enumerate(nums):
        if i > reach:
            return False
        reach = max(reach, i + step)
    return True

print(canJump([2,3,1,1,4]))  # True
print(canJump([3,2,1,0,4]))  # False

