import unittest
from Model.Model import *
from View.View import *
from StringIO import *

class MockMainViewController:
    """mock controller
    """
    def __init__(self, in_file, out_file):
        self.bm = BookManagerModel()
        self.in_file = in_file
        self.out_file = out_file

    def add_book_for_test(self, book):
        self.bm.add_book(book)

    def exit_mainview_callback(self):
        pass

    def sort_book_by_ID(self):
        """sort books by ID
        """
        self.bm.sort_book_by_ID()


    def add_callback(self):
        """add a book
        """
        pass

    def view_callback(self, book):
        """view the book
        """
        pass

    def write(self, msg):
        self.out_file.write(msg)
        
    def readline(self):
        return self.in_file.readline()

    def __iter__(self):
        return self.bm.__iter__()

class ViewTest(unittest.TestCase):
    def setUp(self):
        self.in_file = StringIO()
        self.out_file = StringIO()
        self.controller = MockMainViewController(self.in_file, self.out_file)
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

        b3 = BookModel()
        b3.ID = 1
        b3.name = "zeirdo"
        b3.author = "Job"
        b3.DoP = "2007-7-7"
        b3.DoR = "2009-6-7"
        b3.RoS = 5

        self.controller.add_book_for_test(b1)
        self.controller.add_book_for_test(b2)
        self.controller.add_book_for_test(b3)

    def testMainViewDisplay(self):
        mv = MainView(self.controller)
        mv.load_books()
        mv.display()
        res = self.out_file.getvalue()
        ref = """\
========================================================================================
ID     Name                                    Author          DoP        DoR        RoS
%(books)s
----------------------------------------------------------------------------------------
ID*   : ID, default soft in ID
Name  : Book Name
Author: Author Name
DoP   : Date of Publish
DoR   : Date of Read
RoS   : Review of Score
*     : Key was used in sort 
----------------------------------------------------------------------------------------
Command:
i/I   : sorted in ID
n/N   : sorted in Name
a/A   : sorted in Author
p/P   : sorted in DoP
r/R   : sorted in DoR
s/S   : sorted in RoS
add   : add an item
edit  : edit an item
view  : view an item
find  : find an item by Name
m     : return to main view
p     : previous page, 20 items in a page
n     : next page, 20 items in a page
u     : up item
d     : down item
exit  : exit program
========================================================================================\
        """
        print res
        #self.assertEqual(res, 
        



if __name__ == '__main__':
    unittest.main()
