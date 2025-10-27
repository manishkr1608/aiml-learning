"""
Group Anagrams – LeetCode #49
"""
from collections import defaultdict

def groupAnagrams(strs):
    groups = defaultdict(list)
    for word in strs:
        key = "".join(sorted(word))
        groups[key].append(word)
    return list(groups.values())

# Test
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# [["eat","tea","ate"],["tan","nat"],["bat"]]
