'''
Sort a linked list in O(n log n) time using constant space complexity.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        assert (head)
        pre = None
        cur = head
        nxt = head.next
        while cur != None:
            cur.next = pre
            pre = cur
            cur = nxt
            nxt = nxt.next if nxt else None
        assert (pre)
        assert (not cur)
        assert (not nxt)
        return pre

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

if __name__ == '__main__':
    s1 = ['1', '2', '3', '4', '5', '6']
    l1 = toLinkedList(s1)
    l2 = Solution().sortList(l1)
    l3 = Solution().sortList(l2)
    assert (s1 == toArray(l3))
