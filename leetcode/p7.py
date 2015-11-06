'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
Follow up:
Can you solve it without using extra space?
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
    i = 0
    while p != None:
        s.append(p.val)
        p = p.next
        i = i + 1
        if i > 50:
            break
    return s

def generateCycle(l):
    assert (l)
    p = l
    c = None
    pre = None
    while p != None:
        if (p.val == 5):
            c = p
        pre = p
        p = p.next
    assert (c)
    assert (pre.next == None)
    pre.next = c
    return l

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        assert (head)
        fast = head.next
        slow = head
        while fast != slow:
            if (fast == None or fast.next == None):
                break
            fast = fast.next
            fast = fast.next
            slow = slow.next
        if fast != slow:
            # no cycle
            return None
        assert (fast == slow)
        print fast.val
        
        slow = head
        fast = fast.next
        i = 0
        while fast != slow:
            fast = fast.next
            slow = slow.next
            assert (fast)
            assert (slow)
            i = i + 1
        print i
        return fast

        
if __name__ == '__main__':
    l = toLinkedList(range(20))
    l1 = generateCycle(l)
    print (toArray(l1))
    x = Solution().detectCycle(l1)
    print x.val
