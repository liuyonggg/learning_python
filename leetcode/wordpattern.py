'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
'''

def wordPattern(pattern, str):
    s = pattern
    t = str.split()
    return map(s.find, s) == map(t.index, t)

if __name__ == "__main__":
    assert (wordPattern('abba', 'dog cat cat dog'))
    assert (not wordPattern('abba', 'dog dog cat dog'))
    assert (not wordPattern('abba', 'dog cat cat fish'))
    assert (not wordPattern('aaaa', 'dog cat cat dog'))
    assert (wordPattern('aaaa', 'dog dog dog dog'))
    assert (not wordPattern('abba', 'dog dog dog dog'))
    print ('done')
