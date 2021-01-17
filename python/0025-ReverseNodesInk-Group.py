'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

Follow up:

Could you solve the problem in O(1) extra memory space?
You may not alter the values in the list's nodes, only nodes itself may be changed.
'''



# My Solution (Runtime 99.74%)
def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
    if head.next == None or k == 1:
        return head
    curr = head
    total = 0
    while curr != None:
        curr = curr.next
        total += 1
    count = 0
    curr = head
    prev = None
    while curr != None:
        if total - count < k:
            return head
        if count % k == 0:
            p, rest = self.reverseList(curr, k)
            curr.next = rest
            if count == 0:
                head = p
            else:
                prev.next = p
            count += k - 1
        prev = curr
        curr = curr.next
        count += 1
    return head

def reverseList(self, head: ListNode, total: int) -> (ListNode, ListNode):
    curr = head
    prev = None
    count = 0
    while count < total and curr:
        n = curr.next
        curr.next = prev
        prev = curr
        curr = n
        count += 1
    return prev, curr




# Other Solution (Runtime 50.00%)
def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
    dummy = jump = ListNode(0)
    dummy.next = l = r = head

    while True:
        count = 0
        while r and count < k:   # use r to locate the range
            r = r.next
            count += 1
        if count == k:  # if size k satisfied, reverse the inner linked list
            pre, cur = r, l
            for _ in range(k):
                cur.next, cur, pre = pre, cur.next, cur  # standard reversing
            jump.next, jump, l = pre, l, r  # connect two k-groups
        else:
            return dummy.next
