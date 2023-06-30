# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head == None:
            return False

        fast = head
        slow = head

        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next

            if (id(slow) == id(fast)):
                return True

        return False
