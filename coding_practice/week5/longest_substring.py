"""
Longest Substring Without Repeating Characters - LeetCode #3
"""
def lengthOfLongestSubstring(s):
    seen, start, max_len = {}, 0, 0
    for i, c in enumerate(s):
        if c in seen and seen[c] >= start:
            start = seen[c] + 1
        seen[c] = i
        max_len = max(max_len, i - start + 1)
    return max_len

# Test
print(lengthOfLongestSubstring("abcabcbb"))  # 3 ("abc")
