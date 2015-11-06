'''
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
'''


class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, d):
        assert (len(s))
        m = [False] * len(s)
        for i in xrange(1, len(s)):
            if (m[i] == False and self.containWord(s[0:i+1], d)):
                m[i] = True
            if m[i]:
                for j in xrange(i+1, len(s)):
                    if (m[j] == False and self.containWord(s[i+1:j+1], d)):
                        m[j] = True
                if m[len(s)-1]:
                    return True
        return False
    def containWord(self, w, d):
        return w in d

if __name__ == '__main__':
    s = "catsanddog"
    dict = ["cat", "cats", "and", "sand", "dog"]
    r = Solution().wordBreak(s, dict)
    print r
    s = "catasanddog"
    r = Solution().wordBreak(s, dict)
    print r
