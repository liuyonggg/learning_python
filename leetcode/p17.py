'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
'''

class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        ## palindrome map, {(i, j): True|False} True means substr[i:j-i+1] is palindrome
        palindromeMap = {}
        ## min cut, {(i, j): n} n is min cut of substr[i:j-i+1]
        cut = {}
        for i in xrange(len(s)):
            palindromeMap[(i:i+1)] = True
            cut[(i:i+1)] = 0
        for i in xrange(len(s)):
            for j in xrange(i+1, len(s)):
                if (j == i+1):
                    palindromeMap[(i,j)] = s[i] == s[j]
                else:
                    palindromeMap[(i,j)] = palindromeMap[(i+1,j-1)] && s[i] == s[j]
                    cut[(i,j)] = 0 if palindromeMap[(i,j)] else cut[(i,j-1)]+1
        return 2


if __name__ == '__main__':
    s = 'aab'
    assert (Solution().minCut(s) == 2)
