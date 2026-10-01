# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode(val=-1)
        res = node

        rem = 0
        while l1 or l2:
            tot = rem
            if l1:
                tot += l1.val
                l1 = l1.next
            if l2:
                tot += l2.val
                l2 = l2.next

            rem = tot//10

            node.next = ListNode(val = tot%10)
            node = node.next

        if rem != 0:
            node.next = ListNode(val = rem)

        return res.next
