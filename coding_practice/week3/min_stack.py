
"""
Min Stack - LeetCode #155
Design a stack that supports push, pop, top, and retrieving the minimum in O(1).
"""

class MinStack:
    def __init__(self):
        self.stack, self.min_stack = [], []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        return val

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_stack[-1]

# Quick test
s = MinStack()
s.push(-2); s.push(0); s.push(-3)
print(s.get_min())  # -3
s.pop()
print(s.top())      # 0
print(s.get_min())  # -2
