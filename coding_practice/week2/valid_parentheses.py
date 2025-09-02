"""
Valid Parentheses - LeetCode #20
Input: "()", "()[]{}", "(]"
Output: True, True, False
"""

def is_valid(s: str) -> bool:
    stack = []
    mapping = {")":"(", "]":"[", "}":"{"}
    for ch in s:
        if ch in mapping.values():
            stack.append(ch)
        elif ch in mapping.keys():
            if not stack or stack[-1] != mapping[ch]:
                return False
            stack.pop()
    return not stack

# Tests
print(is_valid("()"))        
print(is_valid("()[]{}"))    
print(is_valid("(]"))        
