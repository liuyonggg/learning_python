'''
Copyright (c) <2015> Zechen Liu
    
    

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:



The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.



THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

import datetime

class Model(object):
    """
    Model for all data
    """
    def __init__(self):
        """ inits the class"""
        pass

    def serialize(self):
        """ serialize the object
        Returns:
            string
        """
        pass

    def deserialize(self, s):
        """ deserialize the object
        Returns:
            object
        """
        return self

class BookModel(Model):
    """
    Model for Book
    """
    def __init__(self):
        """ Inits the model"""
        self._ID = None
        self._name = None
        self._author = None
        self._DoP = None # Date of Publish
        self._DoR = None # Date of Read
        self._RoS = None # Review of Score
    
    def _compare_by_number(self, n1, n2):
        """compare two numbers
        Returns:
            -1 n1 < n2
            0  n1 == n2 
            1  n1 > n2 
        """
        res = 0
        if n1 > n2:
            res = 1
        elif n1 < n2:
            res = -1
        else:
            assert (n1 == n2)
            res = 0
        return res

    def _compare_by_str(self, s1, s2):
        """ compare two str
        Returns:
            -1 s1 < s2
            0  s1 == s2
            1  s1 > s2
        """
        l = len(s1) if len(s1) <= len(s2) else len(s2)
        res = 0
        for i in xrange(l):
            if s1[i] > s2[i]:
                res = 1
                break
            elif s1[i] < s2[i]:
                res = -1
                break
        if res == 0: 
            if len(s1) > len(s2):
                res = 1
            elif len(s1) < len(s2):
                res = -1
            else:
                assert len(s1) == len(s2)
                assert (res == 0)
        return res

    def _compare_by_date(self, d1, d2):
        """compare two numbers
        Returns:
            -1 d1 < d2
            0  d1 == d2 
            1  d1 > d2 
        """
        res = 0
        if d1 > d2:
            res = 1
        elif d1 < d2:
            res = -1
        else:
            assert (d1 == d2)
            res = 0
        return res

        

    def compare_by_ID(self, other):
        """ compare the object with other object by ID
        Returns:
            -1 self._ID < other._ID
            0  self._ID == other._ID
            1  self._ID > other._ID
        """
        return self._compare_by_number(self._ID, other._ID)
        


    def compare_by_name(self, other):
        """ compare the object with other object by name
        Returns:
            -1 self._name < other._name
            0  self._name == other._name
            1  self._name > other._name
        """
        return self._compare_by_str(self._name, other._name)
        

    def compare_by_author(self, other):
        """ compare the object with other object by author
        Returns:
            -1 self._author < other._author
            0  self._author == other._author
            1  self._author > other._author
        """
        return self._compare_by_str(self._author, other._author)

    def compare_by_DoP(self, other):
        """ compare the object with other object by DoP
        Returns:
            -1 self._DoP < other._DoP
            0  self._DoP == other._DoP
            1  self._DoP > other._DoP
        """
        return self._compare_by_date(self._DoP, other._DoP)


    def compare_by_DoR(self, other):
        """ compare the object with other object by DoR
        Returns:
            -1 self._DoR < other._DoR
            0  self._DoR == other._DoR
            1  self._DoR > other._DoR
        """
        return self._compare_by_date(self._DoR, other._DoR)


    def compare_by_RoS(self, other):
        """ compare the object with other object by RoS
        Returns:
            -1 self._RoS < other._RoS
            0  self._RoS == other._RoS
            1  self._RoS > other._RoS
        """
        return self._compare_by_number(self._RoS, other._RoS)

    def get_ID(self):
        """get the ID
        Returns:
            ID
        """
        return self._ID

    def set_ID(self, ID):
        """set the ID
        Returns:
            None
        """
        assert (ID >= 0)
        self._ID = ID

    ID = property(get_ID, set_ID, None, "ID")

    def get_name(self):
        """get the name
        Returns:
            name
        """
        return self._name

    def set_name(self, name):
        """set the name
        Returns:
            None
        """
        assert (name)
        self._name = name
        
        
    def get_author(self):
        """get the author
        Returns:
            author
        """
        return self._author

    def set_author(self, author):
        """set the author
        Returns:
            None
        """
        assert (author)
        self._author = author


    def get_DoP(self):
        """get the DoP
        Returns:
            DoP
        """
        return self._DoP

    def set_DoP(self, DoP):
        """set the DoP
        Returns:
            None
        """
        self._DoP = DoP


    def get_DoR(self):
        """get the DoR
        Returns:
            DoR
        """
        return self._DoR

    def set_DoR(self, DoR):
        """set the DoR
        Returns:
            None
        """
        self._DoR = DoR


    def get_RoS(self):
        """get the RoS
        Returns:
            RoS
        """
        return self._RoS

    def set_RoS(self, RoS):
        """set the RoS
        Returns:
            None
        """
        assert (RoS >= 0)
        self._RoS = RoS

    name = property(get_name, set_name, None, "name")
    author = property(get_author, set_author, None, "author")
    DoP = property(get_DoP, set_DoP, None, "DoP")
    DoR = property(get_DoR, set_DoR, None, "DoR")
    RoS = property(get_RoS, set_RoS, None, "RoS")

    def serialize(self):
        """serialize the object
        Returns:
            string : serialized result
        """
        res = "%d\n%s\n%s\n%s\n%s\n%d\n" % (self._ID, self._name, self._author, self._DoP, self._DoR, self._RoS)
        return res

    def deserialize(self, s):
        """deserialize the object
        Returns:
            None
        """
        a = s.split('\n')
        assert (len(a) == 6 + 1)
        self._ID = int(a[0])
        self._name = a[1]
        self._author = a[2]
        self._DoP = datetime.datetime.strptime(a[3], "%Y-%m-%d").date()
        self._DoR = datetime.datetime.strptime(a[4], "%Y-%m-%d").date()
        self._RoS = int(a[5])
        assert (not a[6])

    def __eq__(self, other):
        """test if self is equal to other
        Returns:
            True : equal
            False : not equal
        """
        return self._ID == other._ID and self._name == other._name and \
                self._author == other._author and self._DoP == other._DoP and  \
                self._DoR == other._DoR and self._RoS == other._RoS
    
    def __str__(self):
        """ convert it to string
        Returns:
            str
        """
        return "%d: %s" % (self.ID, self.name)

    def __repr__(self):
        """ return represent str
        Returns:
            str
        """
        return self.__str__

