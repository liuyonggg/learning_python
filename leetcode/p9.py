import copy
'''
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
'''

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, d):
        assert (len(s))
        for i in xrange(1, len(s)+1):
            if self.containWord(s[0:i], d):
                m = {}
                r=s[0:i]
                self.workBreakRecursive(s, d, i, len(s), m, r)

    def workBreakRecursive(self, s, d, start, end, m, r):
        assert (len(s))
        print (start, end)
        assert (start <= end)
        if start == end:
            print r
        for i in xrange(start, end+1):
            if (start, i) in m or self.containWord(s[start:i], d):
                m[(start, i)] = (start, i)
                r1 = '%s %s' % (r, s[start:i])
                self.workBreakRecursive(s, d, i, end, m, r1)
                
    def containWord(self, w, d):
        return w in d

if __name__ == '__main__':
    s = "catsanddog"
    dict = ["cat", "cats", "and", "sand", "dog"]

    s = "cat"
    Solution().wordBreak(s, dict)

    s = "catsanddog"
    dict = ["cat", "cats", "and", "sand", "dog"]
    Solution().wordBreak(s, dict)
    s = "catasanddog"
    Solution().wordBreak(s, dict)
