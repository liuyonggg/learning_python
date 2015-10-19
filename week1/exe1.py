'this is exercise 1'

def getAt(str, i):
    pass


def find(str, c):
    pass

def getLen(str):
    pass

"for test purpose, student shouldn't change it"
def test1():
    print ("test1: ")
    s = "hello"
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
    print ("all tests passed")
    
