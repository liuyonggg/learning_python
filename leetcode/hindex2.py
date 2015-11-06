'''
For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, his h-index is 3.
Note: If there are several possible values for h, the maximum one is taken as the h-index.
Note: If there are several possible values for h, the maximum one is taken as the h-index.

 What if the citations array is sorted in ascending order? Could you optimize your algorithm?
'''

class Solution():
    def hIndex(self, citations):
        """
        :type citations: List[int], sorted in ascending order list
        :rtype int
        """
        res = 0
        for i in xrange(len(citations)):
            t = len(citations)-i
            m = citations[i] if citations[i] <= t else t
            res = res if res >= m else m
        return res


if __name__ == '__main__':
    assert (Solution().hIndex([1, 2, 3]) == 2)
    assert (Solution().hIndex([1, 2, 3, 4]) == 2)
    assert (Solution().hIndex([1, 2, 3, 4, 5]) == 3)
            
        
