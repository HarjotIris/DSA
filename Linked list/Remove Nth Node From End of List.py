# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        first solution ---->
        if not head:
            return None

        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        if n == length:
            return head.next
        curr = head
        for _ in range(length - n - 1):
            curr = curr.next
                
        if curr and curr.next:
            curr.next = curr.next.next

        return head
        '''

        # Best solution
        dummy = ListNode(0, head)
        fast = slow = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next



        
