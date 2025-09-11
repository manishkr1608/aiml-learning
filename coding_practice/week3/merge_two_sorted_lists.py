"""
Merge Two Sorted Lists – LeetCode #21
Merge two sorted linked lists into one sorted list.
Example: 1->2->4, 1->3->4 → 1->1->2->3->4->4
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = cur = ListNode()
    while l1 and l2:
        if l1.val < l2.val:
            cur.next, l1 = l1, l1.next
        else:
            cur.next, l2 = l2, l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next

# Quick test helper
def to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

a = ListNode(1, ListNode(2, ListNode(4)))
b = ListNode(1, ListNode(3, ListNode(4)))
res = merge_two_lists(a, b)
print(to_list(res))  # [1,1,2,3,4,4]
