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
    class for model
    """
    pass


class BookModel(Model):
    """Model for Book
    """
    def __init__(self):
        """init BookModel
        """
        self._ID = -1
        self._name = ""
        self._author = ""
        self._DoP = ""
        self._DoR = ""
        self._RoS = 8

    def __repr__(self):
        """represent a book
        """
        return "%d\n%s\n%s\n%s\n%s\n%d" % (self.ID, self.name, self.author, self.DoP, self.DoR, self.RoS)
        
    def compare_by_number(self, n1, n2):
        """compares two numbers
        Return:
            0 if number1 is equals to number2
            1 if number1 is bigger than number2
            -1 if number1 is smaller than number2
        """
        if n1 > n2:
            return 1
        elif n2 > n1:
            return -1
        else:
            assert(n1 == n2)
            return 0
    
    def compare_by_string(self, s1, s2):
        """Compare two string
        Returns:
            1 if string1 > string2
            0 if string2 == string2
            -1 if string1 > string2
        """
        if len(s1) < len(s2):
            for i in xrange(len(s1)):
                if s1[i] > s2[i]:
                    return 1
                if s1[i] < s2[i]:
                    return -1
            return 0
        else:
            assert(len(s1) >= len(s2))
            for i in xrange(len(s2)):
                if s1[i] > s2[i]:
                    return 1
                if s1[i] < s2[i]:
                    return -1
            return 0


    def compare_by_ID(self, other):
        """Compare two ID
        Returns:
            1 if self._ID > other._ID
            0 if self._ID == other._ID
            -1 if self._ID > other._ID
        """
        return self.compare_by_number(self._ID, other._ID)

    def compare_by_name(self, other):
        """Compare two name
        Returns:
            1 if self._name > other._name
            0 if self._name == other._name
            -1 if self._name > other._name
        """
        return self.compare_by_string(self._name, other._name)

    def compare_by_author(self, other):
        """Compare two author
        Returns:
            1 if self._author > other._author
            0 if self._author == other._author
            -1 if self._author > other._author
        """
        return self.compare_by_string(self._author, other._author)

    def compare_by_DoP(self, other):
        """Compare two DoP
        Returns:
            1 if self._DoP > other._DoP
            0 if self._DoP == other._DoP
            -1 if self._DoP > other._DoP
        """         
        return self.compare_by_number(self._DoP, other._DoP)

    def compare_by_DoR(self, other):
        """Compare two DoR
        Returns:
            1 if self._DoR > other._DoR
            0 if self._DoR == other._DoR
            -1 if self._DoR > other._DoR
        """         
        return self.compare_by_number(self._DoR, other._DoR)

    def compare_by_RoS(self, other):
        """Compare two RoS
        Returns:
            -1 if self._RoS > other._RoS
            0 if self._RoS == other._RoS
            1 if self._RoS > other._RoS
        """         
        if self._RoS > other._RoS:
            return -1
        elif other._RoS > self._RoS:
            return 1
        else:
            assert(self._RoS == other._RoS)
            return 0

    def get_ID(self):
        """get the ID
        Returns:
            ID
        """
        return self._ID

    def get_author(self):
        """get the author
        Returns:
            author
        """
        return self._author

    def get_name(self):
        """get the name
        Returns:
            name
        """
        return self._name

    def get_DoP(self):
        """get the DoP
        Returns:
            DoP
        """
        return self._DoP

    def get_DoR(self):
        """get the DoR
        Returns:
            DoR
        """
        return self._DoR

    def get_RoS(self):
        """get the RoS
        Returns:
            RoS
        """
        return self._RoS

    def set_ID(self, ID):
        """set the ID
        """
        assert(ID >= 0)
        self._ID = ID
    ID = property(get_ID, set_ID, None, "This is ID's property")

    def set_name(self, name):
        """set the name
        """
        assert(name)
        self._name = name
    name = property(get_name, set_name, None, "This is name's property")

    def set_author(self, author):
        """set the author
        """
        assert(author)
        self._author = author
    author = property(get_author, set_author, None, "This is author's property")

    def set_DoP(self, DoP):
        """set the DoP
        """
        assert(DoP)
        self._DoP = DoP
    DoP = property(get_DoP, set_DoP, None, "This is DoP's property")

    def set_DoR(self, DoR):
        """set the DoR
        """
        assert(DoR)
        self._DoR = DoR
    DoR = property(get_DoR, set_DoR, None, "This is DoR's property")

    def set_RoS(self, RoS):
        """set the RoS
        """
        assert(RoS >= 0)
        self._RoS = RoS
    RoS = property(get_RoS, set_RoS, None, "This is RoS's property")

    def serialize(self):
        """serialize the book
        Return:
            a string containing the book
        """
        return "%d\n%s\n%s\n%s\n%s\n%s\n" % (self._ID, self._name, self._author, self._DoP, self._DoR, self._RoS)

    def deserialize(self, s):
        """deserialize s
        Return:
            a book
        """
        s = s.split("\n")
        assert(len(s) == 7)
        self.ID = int(s[0])
        assert(self.ID >= 0)
        self.name = s[1]
        assert(self.name)
        self.author = s[2]
        assert(self.author)
        self.DoP = s[3]
        assert(self.DoP)
        self.DoR = s[4]
        assert(self.DoR)
        self.RoS = int(s[5])
        assert(self.RoS >= 0)
        #assert(not s[6])

class BookManagerModel(Model):
    """Manager for book
    """
    def __init__(self):
        """init BookManagerModel 
        """
        self.starting_index = 0
        self.books = []
        self.new_ID = len(self.books)
    
    def add_book(self, book):
        """add a book
        """
        book.ID = self.new_ID
        self.new_ID = self.new_ID + 1
        self.books.append(book)
        
    def search_book_by_ID(self, ID):
        """search book by ID
        Returns:
            A book if it's ID is the same as the one entered
            or
            None if no book's ID match the one entered
        """
        for b in self:
            if b.ID == ID:
                return b
        return None

    def search_book_by_name(self, name):
        """search book by name
        Returns:
            A book if it's name is the same as the one entered
            or
            None if no book's name match the one entered
        """
        for i in self:
            if i.name == name: 
                return i
        return None

    def search_book_by_author(self, author):
        """search book by author
        Returns:
            A book if it's author is the same as the one entered
            or
            None if no book's author match the one entered

        """
        for i in self.books:
            if i.author == author: 
                return i
        return None

    def search_book_by_DoP(self, DoP):
        """search book by date of publish
        Returns:
            A book if it's DoP is the same as the one entered
            or
            None if no book's DoP match the one entered
        """
        for i in self.books:
            if i.DoP == DoP:
                return i
        return None

    def search_book_by_DoR(self, DoR):
        """search book by date of read
        Returns:
            A book if it's DoR is the same as the one entered
            or
            None if no book's DoR match the one entered                
        """
        for i in self.books:
            if i.DoR == DoR:
                return i
        return None

    def search_book_by_RoS(self, RoS):
        """search book by review of score
        Returns:
            A book if it's RoS is the same as the one entered
            or
            None if no book's RoS match the one entered
        """
        for i in self.books:
            if i.RoS == RoS:
                return i
        return None

    def merge_sort(self, list_for_sort, sort_function):
        """sort a list
        Returns:
            A sorted list
        """
        if len(list_for_sort) == 1:
            return list_for_sort
        mp = (len(list_for_sort)-1)/2
        l = self.merge_sort(list_for_sort[:mp+1], sort_function)
        r = self.merge_sort(list_for_sort[mp+1:], sort_function)
        self.books = self.merge(l, r, sort_function)
        return self.books

    def merge(self, l1, l2, sort_function):
        """merge two sorted lists
        Returns:
            A sorted list made out of two lists
        """
        res = []
        i = 0
        j = 0
        while i < len(l1) and j < len(l2):
            if sort_function(l1[i], l2[j]) > 0:
                res.append(l2[j])
                j = j + 1
            elif sort_function(l1[i], l2[j]) < 0:
                res.append(l1[i])
                i = i + 1
            elif sort_function(l1[i], l2[j]) == 0:
                res.append(l1[i])
                res.append(l2[j])
                i += 1
                j += 1
        if j == len(l2):
            return res + l1[i:]
        else:
            assert(i == len(l1))
            return res + l2[j:]

    def sort_book_by_ID(self):
        """sort book by ID
        Returns:
            a sorted book list using ID
        """
        return self.merge_sort(self.books, BookModel.compare_by_ID)

    def sort_book_by_name(self):           
        """sort book by name               
        Returns:                         
            a sorted book list using name  
        """                              
        return self.merge_sort(self.books, BookModel.compare_by_name)

    def sort_book_by_author(self):           
        """sort book by author               
        Returns:                         
            a sorted book list using author  
        """                              
        return self.merge_sort(self.books, BookModel.compare_by_author)

    def sort_book_by_DoP(self):           
        """sort book by DoP               
        Returns:                         
            a sorted book list using DoP
        """                              
        return self.merge_sort(self.books, BookModel.compare_by_DoP)

    def sort_book_by_DoR(self):           
        """sort book by DoR               
        Return:                         
            a sorted book list using DoR  
        """                              
        return self.merge_sort(self.books, BookModel.compare_by_DoR)

    def sort_book_by_RoS(self):           
        """sort book by RoS               
        Returns:                         
            a sorted book list using RoS
        """                              
        return self.merge_sort(self.books, BookModel.compare_by_RoS)
    
    def serialize(self):
        """serialize all the books
        Return:
            a string containing all books
        """
        res = ""
        for b in self.books:
            res = res + b.serialize()
        return res

    def deserialize(self, s):
        """deserialize a string
        """
        s = s.split("\n")
        for i in xrange(0, len(s)-1, 6):
            bookstr = "\n".join(s[i:i+6]) + "\n"
            b = BookModel()
            b.deserialize(bookstr)
            self.books.append(b)
        self.new_ID = len(self.books)

    def change_starting_index(self, index):
        """change the starting index
        """
        self.starting_index = index

    def __iter__(self):
        """activate the interator
        """
        return Iterator(self)      

    def number_of_books(self):
        return len(self.books)

class Iterator:
    """a interator
    """

    def __init__(self, bm):
        """init Iterator
        """
        self.index = bm.starting_index
        self.books = bm.books

    def __iter__(self):
        """activate the iterator
        """
        return self

    def next(self):
        """give the next book
        """
        res = None
        if self.index < len(self.books):
                res = self.books[self.index]
                self.index = self.index + 1
                return res
        raise StopIteration()
