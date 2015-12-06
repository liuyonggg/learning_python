import unittest
from Model.Model import *

class BookModelTest(unittest.TestCase):
    def setUp(self):
        self.b1 = BookModel()
        self.b1.ID = 0
        self.b1.name = "weirdo"
        self.b1.author = "Bob"
        self.b1.DoP = "2004-7-7"
        self.b1.DoR = "2005-6-7"
        self.b1.RoS = 0

        self.b2 = BookModel()
        self.b2.ID = 1
        self.b2.name = "zeirdo"
        self.b2.author = "Job"
        self.b2.DoP = "2007-7-7"
        self.b2.DoR = "2009-6-7"
        self.b2.RoS = 5

        self.book = BookModel()
        self.book.ID = 0
        self.book.name = "test"
        self.book.author = "bob"
        self.book.DoP = "1-1-1"
        self.book.DoR = "1-1-1"
        self.book.RoS = 0

        self.b3 = BookModel()
        self.b3.ID = 0
        self.b3.name = "#Cobblestone == LIFE"
        self.b3.author = "Ssundee"
        self.b3.DoP = "2014-4-2"
        self.b3.DoR = "2015-1-5"
        self.b3.RoS = 5

        self.b4 = BookModel()
        self.b4.ID = 0
        self.b4.name = "#Bobby is awesome!"
        self.b4.author = "MrCrainer"
        self.b4.DoP = "2015-8-1"
        self.b4.DoR = "2015-8-7"
        self.b4.RoS = 0

    def test_compare_by_ID(self):
        self.assertEqual(self.b1.compare_by_ID(self.b2), -1)
        self.assertEqual(self.b2.compare_by_ID(self.b1), 1)
        self.b2.ID = 0
        self.assertEqual(self.b2.compare_by_ID(self.b1), 0)

    def test_compare_by_name(self):
        self.assertEqual(self.b1.compare_by_name(self.b2), -1)
        self.assertEqual(self.b2.compare_by_name(self.b1), 1)
        self.b2.name = self.b1.name
        self.assertEqual(self.b2.compare_by_name(self.b1), 0)

    def test_compare_by_author(self):
        self.assertEqual(self.b1.compare_by_author(self.b2), -1)
        self.assertEqual(self.b2.compare_by_author(self.b1), 1)
        self.b2.author = self.b1.author
        self.assertEqual(self.b2.compare_by_author(self.b1), 0)

    def test_compare_by_DoP(self):
        self.assertEqual(self.b1.compare_by_DoP(self.b2), -1)
        self.assertEqual(self.b2.compare_by_DoP(self.b1), 1)
        self.b2.DoP = self.b1.DoP
        self.assertEqual(self.b2.compare_by_DoP(self.b1), 0)

    def test_compare_by_DoR(self):
        self.assertEqual(self.b1.compare_by_DoR(self.b2), -1)
        self.assertEqual(self.b2.compare_by_DoR(self.b1), 1)
        self.b2.DoR = self.b1.DoR
        self.assertEqual(self.b2.compare_by_DoR(self.b1), 0)

    def test_compare_by_RoS(self):
        self.assertEqual(self.b1.compare_by_RoS(self.b2), 1)
        self.assertEqual(self.b2.compare_by_RoS(self.b1), -1)
        self.b2.RoS = self.b1.RoS
        self.assertEqual(self.b2.compare_by_RoS(self.b1), 0)

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
        s1 = self.book.serialize()
        s2 = "0\ntest\nbob\n1-1-1\n1-1-1\n0\n"
        
        self.assertEqual(s1, s2)

    def test_deserialize(self):
        book_copy = BookModel()
        
        a = self.book.serialize()
        book_copy.deserialize(a)
        self.assertEqual(book_copy.ID, 0)
        self.assertEqual(book_copy.name, "test")
        self.assertEqual(book_copy.author, "bob")
        self.assertEqual(book_copy.DoP, "1-1-1")
        self.assertEqual(book_copy.DoR, "1-1-1")
        self.assertEqual(book_copy.RoS, 0)
    
class BookManagerModelTest(unittest.TestCase):
    def setUp(self):
        self.b3 = BookModel()
        self.b3.ID = 0
        self.b3.name = "#Cobblestone == LIFE"
        self.b3.author = "Ssundee"
        self.b3.DoP = "2014-4-2"
        self.b3.DoR = "2015-1-5"
        self.b3.RoS = 5

        self.b4 = BookModel()
        self.b4.ID = 0
        self.b4.name = "#Bobby is awesome!"
        self.b4.author = "MrCrainer"
        self.b4.DoP = "2015-8-1"
        self.b4.DoR = "2015-8-7"
        self.b4.RoS = 0 
   
    def test_add_book(self):
        self.book = BookModel()
        self.book.ID = 0
        self.book.name = "test"
        self.book.author = "bob"
        self.book.DoP = "1-1-1"
        self.book.DoR = "1-1-1"
        self.book.RoS = 0
        test_manager = BookManagerModel()
        test_manager.add_book(self.book) 

    def test_search_book_by_ID(self):
        test = BookManagerModel()
        test.add_book(self.b3)
        self.assertEqual(test.search_book_by_ID(0), test.books[0])

    def test_search_book_by_name(self):
        test = BookManagerModel()
        test.add_book(self.b3)
        self.assertEqual(test.search_book_by_name("#Cobblestone == LIFE"), test.books[0])
        
    def test_search_book_by_author(self):
        test = BookManagerModel()
        test.add_book(self.b3)
        self.assertEqual(test.search_book_by_author("Ssundee"), test.books[0])

    def test_search_book_by_DoP(self):
        test = BookManagerModel()
        test.add_book(self.b3)
        self.assertEqual(test.search_book_by_DoP("2014-4-2"), test.books[0])

    def test_search_book_by_DoR(self):
        test = BookManagerModel()
        test.add_book(self.b3)
        self.assertEqual(test.search_book_by_DoR("2015-1-5"), test.books[0])

    def test_search_book_by_RoS(self):
        test = BookManagerModel()
        test.add_book(self.b3)
        self.assertEqual(test.search_book_by_RoS(5), test.books[0])

    def test_sort_book_by_ID(self):
        test = BookManagerModel()
        test.add_book(self.b3)
        test.add_book(self.b4)
        test.sort_book_by_ID()
        books = [self.b3, self.b4]
        self.assertEqual(test.books, books)

    def test_sort_book_by_name(self):
        test = BookManagerModel()
        test.add_book(self.b3)
        test.add_book(self.b4)
        test.sort_book_by_name()
        books = [self.b4, self.b3]
        self.assertEqual(test.books, books)

    def test_sort_book_by_author(self):
        test = BookManagerModel()
        test.add_book(self.b3)
        test.add_book(self.b4)
        test.sort_book_by_author()
        books = [self.b4, self.b3]
        self.assertEqual(test.books, books)

    def test_sort_book_by_DoP(self):
        test = BookManagerModel()
        test.add_book(self.b3)
        test.add_book(self.b4)
        test.sort_book_by_DoP()
        books = [self.b3, self.b4]
        self.assertEqual(test.books, books)

    def test_sort_book_by_DoR(self):
        test = BookManagerModel()
        test.add_book(self.b3)
        test.add_book(self.b4)
        test.sort_book_by_DoR()
        books = [self.b3, self.b4]
        self.assertEqual(test.books, books)

    def test_sort_book_by_RoS(self):
        test = BookManagerModel()
        test.add_book(self.b3)
        test.add_book(self.b4)
        test.sort_book_by_RoS()
        books = [self.b3, self.b4]
        self.assertEqual(test.books, books)

    def test_serialize(self):
        bm = BookManagerModel()
        bm.add_book(self.b3)
        a = "0\n#Cobblestone == LIFE\nSsundee\n2014-4-2\n2015-1-5\n5\n"
        self.assertEqual(bm.serialize(), a) 

    def test_deserialize(self):
        bm = BookManagerModel()
        self.b4.ID = 1
        a = "0\n#Cobblestone == LIFE\nSsundee\n2014-4-2\n2015-1-5\n5\n1\n#Bobby is awesome!\nMrCrainer\n2015-8-1\n2015-8-7\n0\n"
        bm.deserialize(a)
        self.assertEqual(bm.books[0].ID, self.b3.ID)
        self.assertEqual(bm.books[0].name, self.b3.name)
        self.assertEqual(bm.books[0].author, self.b3.author)
        self.assertEqual(bm.books[0].DoP, self.b3.DoP)
        self.assertEqual(bm.books[0].DoR, self.b3.DoR)
        self.assertEqual(bm.books[0].RoS, self.b3.RoS)
        self.assertEqual(bm.books[1].ID, self.b4.ID)
        self.assertEqual(bm.books[1].name, self.b4.name)
        self.assertEqual(bm.books[1].author, self.b4.author)
        self.assertEqual(bm.books[1].DoP, self.b4.DoP)
        self.assertEqual(bm.books[1].DoR, self.b4.DoR)
        self.assertEqual(bm.books[1].RoS, self.b4.RoS)

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
