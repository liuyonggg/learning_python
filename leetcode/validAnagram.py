'''
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.
'''

import collections

class Solution():
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return list(s).sort() == list(t).sort()

    def isAnagram2(self, s, t):
        return collections.Counter(s) == collections.Counter(t)

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    assert Solution().isAnagram(s, t) == Solution().isAnagram2(s, t)
