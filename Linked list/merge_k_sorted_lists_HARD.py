from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        transition_list = []
        for l in lists:
            if not l:
                continue
            current = l
            while current:
                transition_list.append(current.val)
                current = current.next

        # Edge case: If all lists were empty, return None
        if not transition_list:
            return None

        transition_list.sort()

        new_list = ListNode(transition_list[0])
        new_current = new_list
        for val in transition_list[1:]:
            new_current.next = ListNode(val)
            new_current = new_current.next
        

        return new_list

        
node1 = ListNode(1)
node2 = ListNode(4)
node3 = ListNode(5)
node1.next = node2
node2.next = node3


node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(4)
node4.next = node5
node5.next = node6

node7 = ListNode(2)
node8 = ListNode(6)
node7.next = node8

list_of_lists = [node1, node4, node7]

sol = Solution()
result = sol.mergeKLists(list_of_lists)

def print_linked_list(head):
    current = head  # Start from the head node
    while current:  # Loop until the end of the list
        print(current.val, end=" → ")
        current = current.next  # Move to the next node
    print("None")

print_linked_list(result)
        