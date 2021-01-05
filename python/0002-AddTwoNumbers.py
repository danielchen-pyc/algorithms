'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single
digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.
'''

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    add = l1.val + l2.val
    value = add % 10
    carry = add // 10
    result = ListNode(value)
    first = result
    while (l1.next is not None or l2.next is not None):
        if l1.next == None:
            l1 = ListNode(0)
        else:
            l1 = l1.next
        if l2.next == None:
            l2 = ListNode(0)
        else:
            l2 = l2.next
        add = l1.val + l2.val + carry
        value = add % 10
        carry = add // 10
        result.next = ListNode(value)
        result = result.next
    if carry != 0:
        carryNode = ListNode(carry)
        result.next = carryNode
    return first
