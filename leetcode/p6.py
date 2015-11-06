import copy

'''
Sort a linked list using insertion sort.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def toLinkedList(s):
    assert (len(s))
    h = ListNode(s[0])
    p = h
    for x in s[1::]:
        t = ListNode(x)
        p.next = t
        p = t
    return h

def toArray(link):
    s = []
    p = link
    while p != None:
        s.append(p.val)
        p = p.next
    return s

class NewSolution:
    def insertionSortList(self, head):
        assert (head)
        sortedHead = ListNode(-100000)
        x = head
        while x != None:
            cur = sortedHead
            nxt = sortedHead.next
            while nxt != None:
                if cur.val < x.val and nxt.val >= x.val:
                    break
                cur = nxt
                nxt = nxt.next
            assert (cur.val < x.val and (nxt == None or nxt.val >= x.val))
            cur.next = ListNode(x.val)
            cur.next.next = nxt
            x = x.next
        return sortedHead.next

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        assert (head)
        sortedHead = copy.deepcopy(head)
        sortedHead.next = None
        needInsert = copy.deepcopy(head.next)
        while needInsert != None:
            cur  = None
            nxt  = sortedHead
            while nxt != None:
                if (cur == None or cur.val < needInsert.val) and nxt.val >= needInsert.val:
                    break
                cur = nxt
                nxt = nxt.next
            assert (cur or nxt)
            assert ((cur == None or cur.val < needInsert.val) and (nxt == None or nxt.val >= needInsert.val ))
            if cur:
                cur.next = needInsert
            else:
                cur = needInsert
                sortedHead = cur
            t = needInsert.next
            needInsert.next = nxt
            needInsert = copy.deepcopy(t)
        return sortedHead
    def check(head):
        pass

if __name__ == '__main__':
    s= toLinkedList([2, 9, 1, 10])
    l1 = Solution().insertionSortList(s)
    l2 = NewSolution().insertionSortList(s)
    print (toArray(l2))
    assert (toArray(l1) == toArray(l2))
