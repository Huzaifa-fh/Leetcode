# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 == None and list2 == None: return None

        head = ListNode()
        prev_node = head

        while list1 and list2:
            if list1.val < list2.val:
                val = list1.val
                list1 = list1.next
            else:
                val = list2.val
                list2 = list2.next

            new_node = ListNode(val)
            prev_node.next = new_node
            prev_node = new_node

        remaining_list = list1 if list1 else list2

        while remaining_list:
            new_node = ListNode(remaining_list.val)
            prev_node.next = new_node
            prev_node = new_node

            remaining_list = remaining_list.next

        return head.next

