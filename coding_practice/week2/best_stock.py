"""
Best Time to Buy and Sell Stock - LeetCode #121
Given an array of prices, find max profit from one buy/sell.
Example: [7,1,5,3,6,4] → Output: 5
"""

def max_profit(prices):
    min_price = float("inf")
    profit = 0
    for p in prices:
        min_price = min(min_price, p)
        profit = max(profit, p - min_price)
    return profit

# Tests
print(max_profit([7,1,5,3,6,4]))  # 5
print(max_profit([7,6,4,3,1]))    # 0

