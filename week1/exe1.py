def getAt(str, i):
    '''
    get the ith element in str
    for example: getAt("hello", 0) will return the 0th element 'h' in the "hello"
    :type str: string
    :type i: int
    :rtype char
    '''
    return str[i]


def find(str, c):
    return str.find(c)

def getLen(str):
    return len(str)

def test1():
    print ("test1: ")
    s = "hello"
    assert ('h' == getAt(s, 0))
    assert ('e' == getAt(s, 1))
    assert ('l' == getAt(s, 2))
    assert ('l' == getAt(s, 3))
    assert ('o' == getAt(s, 4))
    i = 0
    for a in s:
        assert (a == getAt(s, i))
        i = i + 1

def test2():
    print ("test2: ")
    s = "hello"
    assert (0 == find(s, 'h'))
    assert (1 == find(s, 'e'))
    assert (2 == find(s, 'l'))
    assert (getAt(s, find(s, 'o')) == 'o')

def test3():
    print ("test3:")
    s = "hello"
    assert (getLen(s) == 5)
    

if __name__ == "__main__":
    test1()
    test2()
    test3()
    
