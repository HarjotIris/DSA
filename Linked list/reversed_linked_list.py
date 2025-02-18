from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        """Helper function to print the list."""
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        stack = []
        while head:
            stack.append(head)
            head = head.next

        new_head = stack.pop()
        current = new_head

        while stack:
            current.next = stack.pop()
            current = current.next
        current.next = None
        return new_head

node1 = ListNode(1)       
node2 = ListNode(2)       
node3 = ListNode(3)       
node4 = ListNode(4)       

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = None
sol = Solution()
print(sol.reverseList(node1))


        
        
