
"""
Top K Frequent Elements – LeetCode #347
"""
import heapq
from collections import Counter

def topKFrequent(nums, k):
    count = Counter(nums)
    return [item for item, _ in heapq.nlargest(k, count.items(), key=lambda x: x[1])]

# Test
print(topKFrequent([1,1,1,2,2,3], 2))  # [1,2]
