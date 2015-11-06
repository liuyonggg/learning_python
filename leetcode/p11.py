'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
'''

class RandomListNode:
    def __init__(self, x, n=None, r=None):
        self.label = x
        self.next = n
        self.random = r

class Solution:
    def copyRandomList(self, head):
        assert (head)
        p = head
        # insert new list
        while p != None:
            n = RandomListNode(p.label, p.next, p.random)
            p.next = n
            p = n.next
        newHead = head.next

        # fix the random link in new list
        p = head
        while p != None:
            p.next.random = p.next.random.next
            p = p.next.next

        # decouple the new list and list
        p = head
        while p != None:
            t = p.next.next
            if p.next.next:
                p.next.next = p.next.next.next
            p.next = t            
            p = t
        return newHead

def genList():
    a =  []
    for i in xrange(0, 10):
        a.append(RandomListNode(i))
    for i in xrange(0, 9):
        a[i].next = a[i+1]
        a[i].random = a[(i*133 + 137) % 10]
    a[9].random = a[(9*133 + 137) % 10]
    return a[0]

def printList(l):
    assert (l)
    p = l
    while p != None:
        if p.next:
            print ("label = %s, next label = %s, random label = %s" % (p.label, p.next.label if p.next else None, p.random.label))
        else:
            print ("label = %s, next label = %s, random label = %s" % (p.label, None, p.random.label))
        p = p.next

if __name__ == '__main__':
    l1 = genList()
    printList(l1)
    l2 = Solution().copyRandomList(l1)
    printList(l2)
