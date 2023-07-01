# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode()
        prev_node = head

        carry = 0

        while l1 and l2:
            sum_ = l1.val + l2.val + carry
            remainder = sum_ % 10

            new_node = ListNode(remainder)

            carry = sum_ // 10
            prev_node.next = new_node
            prev_node = new_node

            l1 = l1.next
            l2 = l2.next

        remaining_list = l1 if l1 else l2

        while remaining_list:
            sum_ = remaining_list.val + carry
            remainder = sum_ % 10

            new_node = ListNode(remainder)

            carry = sum_ // 10
            prev_node.next = new_node
            prev_node = new_node
            remaining_list = remaining_list.next

        if carry != 0:
            new_node = ListNode(carry)
            prev_node.next = new_node

        return head.next
