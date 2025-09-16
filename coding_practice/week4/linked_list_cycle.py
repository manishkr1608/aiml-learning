"""
Linked List Cycle – LeetCode #141
Detect if a linked list has a cycle in it.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head: ListNode) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast:
            return True
    return False

# Test
a = ListNode(3)
b = ListNode(2)
c = ListNode(0)
d = ListNode(-4)
a.next, b.next, c.next, d.next = b, c, d, b  # cycle at node b
print(has_cycle(a))  # True
