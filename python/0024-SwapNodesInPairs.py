'''
Given a linked list, swap every two adjacent nodes and return its head.
'''


# My Solution (Runtime 83.69%)
def swapPairs(self, head: ListNode) -> ListNode:
    count = 0
    if not head or not head.next:
        return head
    curr = head
    head = curr.next
    prev = ListNode()
    prev.next = curr
    while curr:
        if curr.next:
            if count == 0:
                prev = curr.next
            else:
                prev.next = curr.next
                prev = prev.next
            curr.next = curr.next.next
            prev.next = curr
        prev = prev.next
        curr = curr.next
        count += 1
    return head



# Other Solution (Runtime 57.71%)
def swapPairs(self, head: ListNode) -> ListNode:
    pre, pre.next = self, head
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        pre.next, b.next, a.next = b, a, b.next
        pre = a
    return self.next
