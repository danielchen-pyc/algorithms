'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
'''



# My Solution (Runtime 44.06%)
def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if None in lists:
            lists.remove(None)
        if len(lists) == 0 or (lists[0] == None):
            return None
        return self.partition(lists)[0]


def partition(self, lists: List[ListNode]) -> List[ListNode]:
    if len(lists) == 0:
        return [None]
    elif len(lists) == 1:
        return lists
    else:
        left = self.partition(lists[:int(len(lists)/2)])
        right = self.partition(lists[int(len(lists)/2):])
        return [self.mergeTwoLists(left[0], right[0])]


def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if not l1 or not l2:
        return l1 or l2
    if l1.val <= l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2



# Other Solution (Runtime 75.84%)
def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    heads = []
    for idx, lst in enumerate(lists):
        if lst: heapq.heappush(heads, (lst.val, idx))

    result = ListNode(-1)
    temp = result

    while heads:
        smval, smidx = heapq.heappop(heads)
        temp.next = lists[smidx]
        temp = temp.next
        if lists[smidx].next:
            lists[smidx] = lists[smidx].next
            heapq.heappush(heads, (lists[smidx].val, smidx))


# Other Solution (Runtime 75.84%)
def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    h = []
    while None in lists:
        lists.remove(None)
    if len(lists) == 0 or (lists[0] == None):
        return None
    head = tail = ListNode(0)
    for i in range(len(lists)):
        heapq.heappush(h, (lists[i].val, i, lists[i]))

    while h:
        node = heapq.heappop(h)
        node = node[2]
        tail.next = node
        tail = tail.next
        if node.next:
            i+=1
            heapq.heappush(h, (node.next.val, i, node.next))

    return head.next
