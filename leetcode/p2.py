'''
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".
'''

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        a = s.split()
        b = ' '.join(a[i] for i in xrange(len(a)-1, -1, -1))
        return b

if __name__ == "__main__":
    assert(Solution().reverseWords("the sky is blue") == "blue is sky the")
    assert(Solution().reverseWords("") == "")
