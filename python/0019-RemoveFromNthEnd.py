'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''


# My Solution (Runtime 47.44%)
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    curr = head
    total = 0
    while curr != None:
        total += 1
        curr = curr.next
    count = 0
    curr = head
    if total == 1 and n == 1:
        curr = None
        return curr
    elif total == n:
        head = head.next
        return head
    while count != total:
        diff = total - count - 1
        if diff == n:
            if curr.next != None:
                curr.next = curr.next.next
            else:
                curr.next = None
            return head
        count += 1
        curr = curr.next
    return head


# Runtime 92.58%
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    if not n: return head
    l=[]
    while head:
        l+=[head.val]
        head=head.next
    del l[-n]
    l.reverse()
    t=None
    for elt in l:
        t= ListNode(elt,t)
    return t
