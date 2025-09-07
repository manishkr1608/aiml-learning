"""
Reinforcement Practice – Combine concepts
1. Two Sum variation: Return indices of 3 numbers summing to target
2. Stock variation: Allow at most 2 transactions
"""

# --- Problem 1: Three Sum indices ---
def three_sum(nums, target):
    nums = [(n, i) for i, n in enumerate(nums)]
    nums.sort()
    n = len(nums)
    for i in range(n):
        l, r = i+1, n-1
        while l < r:
            total = nums[i][0] + nums[l][0] + nums[r][0]
            if total == target:
                return [nums[i][1], nums[l][1], nums[r][1]]
            elif total < target:
                l += 1
            else:
                r -= 1
    return []

print(three_sum([1,2,3,4,5], 9))  # [0,2,4] or similar

# --- Problem 2: Max profit with 2 transactions ---
def max_profit_two(prices):
    buy1 = buy2 = float("inf")
    profit1 = profit2 = 0
    for p in prices:
        buy1 = min(buy1, p)
        profit1 = max(profit1, p - buy1)
        buy2 = min(buy2, p - profit1)
        profit2 = max(profit2, p - buy2)
    return profit2

print(max_profit_two([3,3,5,0,0,3,1,4]))  # 6
