class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
def has_cycle(head):
    # no cycle if the head is empty, or if there is
    # only one node

    if not head or not head.next:
        return False
    
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False

# create nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

# connect nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

print(has_cycle(node1))
