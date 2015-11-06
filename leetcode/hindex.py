'''
For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, his h-index is 3.
Note: If there are several possible values for h, the maximum one is taken as the h-index.
Note: If there are several possible values for h, the maximum one is taken as the h-index.
'''
class Solution():
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        return max([min(k+1, v) for (k, v) in enumerate(citations)]) if citations else 0

class Solution2():
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citation_article_table = [0]*(len(citations)+1)
        for i in xrange(len(citations)):
            if citations[i] > len(citations):
                citation_article_table[len(citations)] += 1
            else:
                citation_article_table[citations[i]] += 1
        s = 0
        for i in xrange(len(citations), -1, -1):
            s += citation_article_table[i]
            if s >= i:
                return i
        return 0
            


if __name__ == '__main__':
    assert (Solution().hIndex([1, 2, 3]) == 2)
    assert (Solution().hIndex([1, 2, 3]) == Solution2().hIndex([1,2,3]))

        
