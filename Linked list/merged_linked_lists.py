# Definition for singly-linked list.
from typing import Optional
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, val):
        new_node = ListNode(val)

        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print(self):
        current = self.head
        while current:
            print(current.val, end = " -> ")
            current = current.next
        print("None")


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> LinkedList:
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list

sol = Solution()
l1 = LinkedList()
l1.append(1)
l1.append(2)
l1.append(4)

l2 = LinkedList()
l2.append(1)
l2.append(3)
l2.append(5)

print("First sorted list")
l1.print()
print("Second sorted list")
l2.print()

merged = sol.mergeTwoLists(l1.head, l2.head)
print("Merged list")
merged.print()