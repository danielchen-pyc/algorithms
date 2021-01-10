'''
Merge two sorted linked lists and return it as a sorted list. The list should be
made by splicing together the nodes of the first two lists.
'''


# My Solution (Runtime 73.97%)
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if l1 == None:
        return l2
    if l2 == None:
        return l1
    head = ListNode(l1.val) if l1.val >= l2.val else ListNode(l2)
    prev = head
    while l1 and l2:
        if l1.val <= l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        prev = prev.next
    if l1:
        while l1:
            prev.next = l1
            l1 = l1.next
            prev = prev.next
    if l2:
        while l2:
            prev.next = l2
            l2 = l2.next
            prev = prev.next
    return head.next
