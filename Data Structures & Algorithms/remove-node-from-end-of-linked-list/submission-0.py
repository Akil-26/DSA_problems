# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        Left = dummy
        Right = head

        while n>0:
            Right = Right.next
            n -= 1
        
        while Right:
            Left = Left.next
            Right = Right.next
        
        Left.next = Left.next.next
        return dummy.next