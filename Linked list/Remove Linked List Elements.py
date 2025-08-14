# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        '''

        dummy = ListNode(0)
        dummy.next = head

        current = dummy
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next
        '''
        '''
        if not head:
            return None

        head.next = self.removeElements(head.next, val)

        if head.val == val:
            return head.next

        else:
            return head
        '''
        prev = None
        new_head = None

        while head != None:
            if head.val == val:
                if prev:
                    prev.next = head.next
            else:
                prev = head
                if not new_head:
                    new_head = head

            head = head.next
        return new_head