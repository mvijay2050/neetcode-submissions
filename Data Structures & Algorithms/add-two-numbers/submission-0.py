# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        dummy = ListNode(0) 
        current = dummy
        while l1  or l2 :
            
            val1 = 0
            if l1 :
                val1 = l1.val
                l1 = l1.next
            val2 = 0
            if l2 :
                val2 = l2.val
                l2 = l2.next

            sum = val1 + val2 + carry
            if sum > 9:
                carry = 1
                sum = sum%10
            else:
                carry = 0

            current.next = ListNode(sum)
            current = current.next

        if carry > 0:
            current.next = ListNode(carry)
        return dummy.next
