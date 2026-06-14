# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head):
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next  
            curr.next = prev 
            prev = curr      
            curr = nxt       
            
        return prev 

    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0

        slow = head
        fast = head    

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head1 = self.reverse(slow)

        val = 0
        while head1 and head:
            val = max(val, head.val + head1.val)
            head = head.next
            head1 = head1.next

        return val
        

        


