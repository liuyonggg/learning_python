'''
Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().

Here is an example. Assume that the iterator is initialized to the beginning of the list: [1, 2, 3].

Call next() gets you 1, the first element in the list.

Now you call peek() and it returns 2, the next element. Calling next() after that still return 2.

You call next() the final time and it returns 3, the last element. Calling hasNext() after that should return false.

'''

# Below is the interface for Iterator, which is already defined for you.
#
class Iterator(object):
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.iterator = iter(nums)
        self.end = False
        self.nx = None
        

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        if not self.nx:
            self.nx = self.next()
            self.end = self.nx is None
        return not self.end
        


    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        res = None
        if self.nx:
            res = self.nx
            self.nx = None
        else:
            try:
                res = self.iterator.next()
            except StopIteration:
                pass
        return res

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.peekObj = None
        self.peeked = False
        self.iterator = iterator

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.peeked:
            self.peeked = self.iterator.hasNext()
            self.peekObj = self.iterator.next() if self.iterator.hasNext() else None
        return self.peekObj

    def next(self):
        """
        :rtype: int
        """
        res = None
        if self.peeked:
            res = self.peekObj
        else:
            res = self.iterator.next() if self.iterator.hasNext() else None
        self.peeked = False
        self.peekObj = None
        return res


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.peeked or self.iterator.hasNext()

        



# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].

if __name__ == "__main__":
    it = Iterator([1, 2])
    assert it.hasNext()
    assert it.next() == 1
    assert it.hasNext()
    assert it.next() == 2
    assert not it.hasNext()
    pi = PeekingIterator(Iterator([1, 2]))
    assert pi.peek() == pi.peek()
    assert pi.peeked == True
    assert pi.peek() == pi.next()
    assert pi.hasNext()
    assert pi.peeked == False
    assert pi.peek() == pi.peek()
    assert pi.peeked == True
    assert pi.hasNext()
    assert pi.peek() == pi.next()
    assert not pi.hasNext()
    assert not pi.peek()
