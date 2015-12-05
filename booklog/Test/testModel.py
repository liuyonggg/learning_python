import unittest
from Model.Model import *

class BookModelTest(unittest.TestCase):
    def test_compare_by_ID(self):
        b1 = BookModel()
        b1.ID = 0
        b1.name = "weirdo"
        b1.author = "Bob"
        b1.DoP = "2004-7-7"
        b1.DoR = "2005-6-7"
        b1.RoS = 0

        b2 = BookModel()
        b2.ID = 1
        b2.name = "zeirdo"
        b2.author = "Job"
        b2.DoP = "2007-7-7"
        b2.DoR = "2009-6-7"
        b2.RoS = 5

        self.assertEqual(b1.compare_by_ID(b2), -1)
        self.assertEqual(b2.compare_by_ID(b1), 1)
        b2.ID = 0
        self.assertEqual(b2.compare_by_ID(b1), 0)

    def test_compare_by_name(self):
        b1 = BookModel()
        b1.ID = 0
        b1.name = "weirdo"
        b1.author = "Bob"
        b1.DoP = "2004-7-7"
        b1.DoR = "2005-6-7"
        b1.RoS = 0

        b2 = BookModel()
        b2.ID = 1
        b2.name = "zeirdo"
        b2.author = "Job"
        b2.DoP = "2007-7-7"
        b2.DoR = "2009-6-7"
        b2.RoS = 5

        self.assertEqual(b1.compare_by_name(b2), -1)
        self.assertEqual(b2.compare_by_name(b1), 1)
        b2.name = b1.name
        self.assertEqual(b2.compare_by_name(b1), 0)

    def test_compare_by_author(self):
        b1 = BookModel()
        b1.ID = 0
        b1.name = "weirdo"
        b1.author = "Bob"
        b1.DoP = "2004-7-7"
        b1.DoR = "2005-6-7"
        b1.RoS = 0

        b2 = BookModel()
        b2.ID = 1
        b2.name = "zeirdo"
        b2.author = "Job"
        b2.DoP = "2007-7-7"
        b2.DoR = "2009-6-7"
        b2.RoS = 5

        self.assertEqual(b1.compare_by_author(b2), -1)
        self.assertEqual(b2.compare_by_author(b1), 1)
        b2.author = b1.author
        self.assertEqual(b2.compare_by_author(b1), 0)

    def test_compare_by_DoP(self):
        b1 = BookModel()
        b1.ID = 0
        b1.name = "weirdo"
        b1.author = "Bob"
        b1.DoP = "2004-7-7"
        b1.DoR = "2005-6-7"
        b1.RoS = 0

        b2 = BookModel()
        b2.ID = 1
        b2.name = "zeirdo"
        b2.author = "Job"
        b2.DoP = "2007-7-7"
        b2.DoR = "2009-6-7"
        b2.RoS = 5

        self.assertEqual(b1.compare_by_DoP(b2), -1)
        self.assertEqual(b2.compare_by_DoP(b1), 1)
        b2.DoP = b1.DoP
        self.assertEqual(b2.compare_by_DoP(b1), 0)

    def test_compare_by_DoR(self):
        b1 = BookModel()
        b1.ID = 0
        b1.name = "weirdo"
        b1.author = "Bob"
        b1.DoP = "2004-7-7"
        b1.DoR = "2005-6-7"
        b1.RoS = 0

        b2 = BookModel()
        b2.ID = 1
        b2.name = "zeirdo"
        b2.author = "Job"
        b2.DoP = "2007-7-7"
        b2.DoR = "2009-6-7"
        b2.RoS = 5

        self.assertEqual(b1.compare_by_DoR(b2), -1)
        self.assertEqual(b2.compare_by_DoR(b1), 1)
        b2.DoR = b1.DoR
        self.assertEqual(b2.compare_by_DoR(b1), 0)

    def test_compare_by_RoS(self):
        b1 = BookModel()
        b1.ID = 0
        b1.name = "weirdo"
        b1.author = "Bob"
        b1.DoP = "2004-7-7"
        b1.DoR = "2005-6-7"
        b1.RoS = 0

        b2 = BookModel()
        b2.ID = 1
        b2.name = "zeirdo"
        b2.author = "Job"
        b2.DoP = "2007-7-7"
        b2.DoR = "2009-6-7"
        b2.RoS = 5

        self.assertEqual(b1.compare_by_RoS(b2), 1)
        self.assertEqual(b2.compare_by_RoS(b1), -1)
        b2.RoS = b1.RoS
        self.assertEqual(b2.compare_by_RoS(b1), 0)

    def test_get_ID(self):
        test = BookModel()
        test.ID = 9
        self.assertEqual(test.get_ID(), 9)

    def test_get_name(self):
        test = BookModel()
        test.name = "zeiro"
        self.assertEqual(test.get_name(), "zeiro")

    def test_get_author(self):
        test = BookModel()
        test.author = "boblina"
        self.assertEqual(test.get_author(), "boblina")

    def test_get_DoP(self):
        test = BookModel()
        test.DoP = "2015-3-8"
        self.assertEqual(test.get_DoP(), "2015-3-8")

    def test_get_DoR(self):
        test = BookModel()
        test.DoR = "1-1-1"
        self.assertEqual(test.get_DoR(), "1-1-1")

    def test_get_RoS(self):
        test = BookModel()
        test.RoS = "0"
        self.assertEqual(test.get_RoS(), "0")

    def test_serialize(self):
        book = BookModel()
        book.ID = 0
        book.name = "test"
        book.author = "bob"
        book.DoP = "1-1-1"
        book.DoR = "1-1-1"
        s1 = book.serialize()
        s2 = "0\ntest\nbob\n1-1-1\n1-1-1\n0\n"
        
        self.assertEqual(s1, s2)
        #self.assertEqual(book.serialize(), book)

    def test_deserialize(self):
        book = BookModel()
        book_copy = BookModel()
        book.ID = 0
        book.name = "test"
        book.author = "bob"
        book.DoP = "1-1-1"
        book.DoR = "1-1-1"
        book.RoS = 0
        
        a = book.serialize()
        book_copy.deserialize(a)
        self.assertEqual(book_copy.ID, 0)
        self.assertEqual(book_copy.name, "test")
        self.assertEqual(book_copy.author, "bob")
        self.assertEqual(book_copy.DoP, "1-1-1")
        self.assertEqual(book_copy.DoR, "1-1-1")
        self.assertEqual(book_copy.RoS, 0)
    
class BookManagerModelTest(unittest.TestCase):
    def test_add_book(self):
        book = BookModel()
        book.ID = 0
        book.name = "test"
        book.author = "bob"
        book.DoP = "1-1-1"
        book.DoR = "1-1-1"
        test_manager = BookManagerModel()
        test_manager.add_book(book) 

    def test_search_book_by_ID(self):
        book = BookModel()
        book.ID = 0
        book.name = "#Cobblestone == LIFE"
        book.author = "Ssundee"
        book.DoP = "2014-4-2"
        book.DoR = "2015-1-5"
        book.RoS = 5

        test = BookManagerModel()
        test.add_book(book)
        self.assertEqual(test.search_book_by_ID(0), test.books[0])

    def test_search_book_by_name(self):
        book = BookModel()
        book.ID = 0
        book.name = "#Cobblestone == LIFE"
        book.author = "Ssundee"
        book.DoP = "2014-4-2"
        book.DoR = "2015-1-5"
        book.RoS = 5

        test = BookManagerModel()
        test.add_book(book)
        self.assertEqual(test.search_book_by_name("#Cobblestone == LIFE"), test.books[0])
        
    def test_search_book_by_author(self):
        book = BookModel()
        book.ID = 0
        book.name = "#Cobblestone == LIFE"
        book.author = "Ssundee"
        book.DoP = "2014-4-2"
        book.DoR = "2015-1-5"
        book.RoS = 5

        test = BookManagerModel()
        test.add_book(book)
        self.assertEqual(test.search_book_by_author("Ssundee"), test.books[0])

    def test_search_book_by_DoP(self):
        book = BookModel()
        book.ID = 0
        book.name = "#Cobblestone == LIFE"
        book.author = "Ssundee"
        book.DoP = "2014-4-2"
        book.DoR = "2015-1-5"
        book.RoS = 5

        test = BookManagerModel()
        test.add_book(book)
        self.assertEqual(test.search_book_by_DoP("2014-4-2"), test.books[0])

    def test_search_book_by_DoR(self):
        book = BookModel()
        book.ID = 0
        book.name = "#Cobblestone == LIFE"
        book.author = "Ssundee"
        book.DoP = "2014-4-2"
        book.DoR = "2015-1-5"
        book.RoS = 5

        test = BookManagerModel()
        test.add_book(book)
        self.assertEqual(test.search_book_by_DoR("2015-1-5"), test.books[0])

    def test_search_book_by_RoS(self):
        book = BookModel()
        book.ID = 0
        book.name = "#Cobblestone == LIFE"
        book.author = "Ssundee"
        book.DoP = "2014-4-2"
        book.DoR = "2015-1-5"
        book.RoS = 5

        test = BookManagerModel()
        test.add_book(book)
        self.assertEqual(test.search_book_by_RoS(5), test.books[0])

    def test_sort_book_by_ID(self):
        book1 = BookModel()
        book1.ID = 1
        book1.name = "#Cobblestone == LIFE"
        book1.author = "Ssundee"
        book1.DoP = "2014-4-2"
        book1.DoR = "2015-1-5"
        book1.RoS = 5

        book2 = BookModel()
        book2.ID = 0
        book2.name = "#Bobby is awesome!"
        book2.author = "MrCrainer"
        book2.DoP = "2015-8-1"
        book2.DoR = "2015-8-7"
        book2.RoS = 0

        test = BookManagerModel()
        test.add_book(book1)
        test.add_book(book2)
        test.sort_book_by_ID()
        books = [book1, book2]
        self.assertEqual(test.books, books)

    def test_sort_book_by_name(self):
        book1 = BookModel()
        book1.ID = 0
        book1.name = "#Cobblestone == LIFE"
        book1.author = "Ssundee"
        book1.DoP = "2014-4-2"
        book1.DoR = "2015-1-5"
        book1.RoS = 5

        book2 = BookModel()
        book2.ID = 1
        book2.name = "#Bobby is awesome!"
        book2.author = "MrCrainer"
        book2.DoP = "2015-8-1"
        book2.DoR = "2015-8-7"
        book2.RoS = 0

        test = BookManagerModel()
        test.add_book(book1)
        test.add_book(book2)
        test.sort_book_by_name()
        books = [book2, book1]
        self.assertEqual(test.books, books)

    def test_sort_book_by_author(self):
        book1 = BookModel()
        book1.ID = 1
        book1.name = "#Cobblestone == LIFE"
        book1.author = "Ssundee"
        book1.DoP = "2014-4-2"
        book1.DoR = "2015-1-5"
        book1.RoS = 5

        book2 = BookModel()
        book2.ID = 0
        book2.name = "#Bobby is awesome!"
        book2.author = "MrCrainer"
        book2.DoP = "2015-8-1"
        book2.DoR = "2015-8-7"
        book2.RoS = 0

        test = BookManagerModel()
        test.add_book(book1)
        test.add_book(book2)
        test.sort_book_by_author()
        books = [book2, book1]
        self.assertEqual(test.books, books)

    def test_sort_book_by_DoP(self):
        book1 = BookModel()
        book1.ID = 1
        book1.name = "#Cobblestone == LIFE"
        book1.author = "Ssundee"
        book1.DoP = "2014-4-2"
        book1.DoR = "2015-1-5"
        book1.RoS = 5

        book2 = BookModel()
        book2.ID = 0
        book2.name = "#Bobby is awesome!"
        book2.author = "MrCrainer"
        book2.DoP = "2015-8-1"
        book2.DoR = "2015-8-7"
        book2.RoS = 0

        test = BookManagerModel()
        test.add_book(book1)
        test.add_book(book2)
        test.sort_book_by_DoP()
        books = [book1, book2]
        self.assertEqual(test.books, books)

    def test_sort_book_by_DoR(self):
        book1 = BookModel()
        book1.ID = 1
        book1.name = "#Cobblestone == LIFE"
        book1.author = "Ssundee"
        book1.DoP = "2014-4-2"
        book1.DoR = "2015-1-5"
        book1.RoS = 5

        book2 = BookModel()
        book2.ID = 0
        book2.name = "#Bobby is awesome!"
        book2.author = "MrCrainer"
        book2.DoP = "2015-8-1"
        book2.DoR = "2015-8-7"
        book2.RoS = 0

        test = BookManagerModel()
        test.add_book(book1)
        test.add_book(book2)
        test.sort_book_by_DoR()
        books = [book1, book2]
        self.assertEqual(test.books, books)

    def test_sort_book_by_RoS(self):
        book1 = BookModel()
        book1.ID = 1
        book1.name = "#Cobblestone == LIFE"
        book1.author = "Ssundee"
        book1.DoP = "2014-4-2"
        book1.DoR = "2015-1-5"
        book1.RoS = 5

        book2 = BookModel()
        book2.ID = 0
        book2.name = "#Bobby is awesome!"
        book2.author = "MrCrainer"
        book2.DoP = "2015-8-1"
        book2.DoR = "2015-8-7"
        book2.RoS = 0

        test = BookManagerModel()
        test.add_book(book1)
        test.add_book(book2)
        test.sort_book_by_RoS()
        books = [book1, book2]
        self.assertEqual(test.books, books)

    def test_serialize(self):
        book1 = BookModel()
        bm = BookManagerModel()
        book1.ID = 0
        book1.name = "#Cobblestone == LIFE"
        book1.author = "Ssundee"
        book1.DoP = "2014-4-2"
        book1.DoR = "2015-1-5"
        book1.RoS = 5
        bm.add_book(book1)
        a = "0\n#Cobblestone == LIFE\nSsundee\n2014-4-2\n2015-1-5\n5\n"
        self.assertEqual(bm.serialize(), a) 

    def test_deserialize(self):
        book1 = BookModel()
        book1.ID = 0
        book1.name = "#Cobblestone == LIFE"
        book1.author = "Ssundee"
        book1.DoP = "2014-4-2"
        book1.DoR = "2015-1-5"
        book1.RoS = 5

        book2 = BookModel()
        book2.ID = 1
        book2.name = "#Bobby is awesome!"
        book2.author = "MrCrainer"
        book2.DoP = "2015-8-1"
        book2.DoR = "2015-8-7"
        book2.RoS = 0

        bm = BookManagerModel()
        a = "0\n#Cobblestone == LIFE\nSsundee\n2014-4-2\n2015-1-5\n5\n1\n#Bobby is awesome!\nMrCrainer\n2015-8-1\n2015-8-7\n0\n"
        bm.deserialize(a)
        print "debug start"
        print bm.books[0]
        print book1
        print "debug end"
        self.assertEqual(bm.books[0].ID, book1.ID)
        self.assertEqual(bm.books[0].name, book1.name)
        self.assertEqual(bm.books[0].author, book1.author)
        self.assertEqual(bm.books[0].DoP, book1.DoP)
        self.assertEqual(bm.books[0].DoR, book1.DoR)
        self.assertEqual(bm.books[0].RoS, book1.RoS)
        self.assertEqual(bm.books[1].ID, book2.ID)
        self.assertEqual(bm.books[1].name, book2.name)
        self.assertEqual(bm.books[1].author, book2.author)
        self.assertEqual(bm.books[1].DoP, book2.DoP)
        self.assertEqual(bm.books[1].DoR, book2.DoR)
        self.assertEqual(bm.books[1].RoS, book2.RoS)

class TestInterator(unittest.TestCase):
    def test_next(self):
        book = BookModel()
        book.ID = 0
        book.name = "#Bobby is awesome!"
        book.author = "MrCrainer"
        book.DoP = "2015-8-1"
        book.DoR = "2015-8-7"
        book.RoS = 0
        bm = BookManagerModel()
        bm.add_book(book)

        for i in bm:
            self.assertEqual(i, book)

if __name__ == '__main__':
    unittest.main()
