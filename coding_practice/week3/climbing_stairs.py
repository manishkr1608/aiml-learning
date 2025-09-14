"""
Climbing Stairs - LeetCode #70
You can climb 1 or 2 steps at a time. How many ways to reach the top?
Example: n=3 → 3 ways (1+1+1, 1+2, 2+1)
"""

def climb_stairs(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n+1):
        a, b = b, a+b
    return b

# Tests
print(climb_stairs(2))  # 2
print(climb_stairs(3))  # 3
print(climb_stairs(5))  # 8
