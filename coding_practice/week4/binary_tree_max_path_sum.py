"""
Binary Tree Maximum Path Sum - LeetCode #124
Find the maximum path sum in a binary tree.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def maxPathSum(root: TreeNode) -> int:
    max_sum = float("-inf")
    
    def dfs(node):
        nonlocal max_sum
        if not node: return 0
        left = max(dfs(node.left), 0)
        right = max(dfs(node.right), 0)
        max_sum = max(max_sum, node.val + left + right)
        return node.val + max(left, right)
    
    dfs(root)
    return max_sum

# Test
root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(maxPathSum(root))  # 42
