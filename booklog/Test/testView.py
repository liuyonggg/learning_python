import unittest
from Model.Model import *
from View.View import *
from StringIO import *

class MockMainViewController:
    """mock controller
    """
    def __init__(self, in_file, out_file):
        self.mv = MainView(self)
        self.bm = BookManagerModel()
        self.in_file = in_file
        self.out_file = out_file
        self.inValues = ""
        self.inValuesIndex = 0

    def add_book(self, book):
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

    def find_callback(self, name):
        return self.bm.search_book_by_name(name)

    def write(self, msg):
        self.out_file.write(msg)
        
    def getvalue(self):
        ret = self.inValues[self.inValuesIndex]
        self.inValuesIndex = self.inValuesIndex + 1
        return ret

    def __iter__(self):
        return self.bm.__iter__()

    def run(self):
        self.mv.display()
        self.mv.handler()

    def setInputValue(self, s):
        self.inValues = s.split('\n')
        self.inValuesIndex = 0

    def validate_book(self, type, name, author, DoP, DoR, RoS):
        if type == "add":
            return name and author and DoP and DoR and RoS != None and RoS.isdigit()
        elif type == "edit":
            return RoS.isdigit()

class ViewTest(unittest.TestCase):
    def setUp(self):
        self.in_file = StringIO()
        self.out_file = StringIO()
        self.controller = MockMainViewController(self.in_file, self.out_file)
        b1 = BookModel()
        b1.ID = 7
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
        b3.ID = 9993840
        b3.name = "zeirdo"
        b3.author = "Job"
        b3.DoP = "2007-7-7"
        b3.DoR = "2009-6-7"
        b3.RoS = 5

        self.controller.add_book(b1)
        self.controller.add_book(b2)
        self.controller.add_book(b3)

    def testMainView(self):
        mv = MainView(self.controller)
        mv.load_books()
        mv.display()
        res = self.out_file.getvalue()
        ref = '''\
=========================================================================================
*ID    name                                     author          DoP        DoR        RoS 
_0     weirdo                                   Bob             2004-7-7   2005-6-7   0   
 1     zeirdo                                   Job             2007-7-7   2009-6-7   5   
 2     zeirdo                                   Job             2007-7-7   2009-6-7   5   

-----------------------------------------------------------------------------------------
ID*    : ID, default sort in ID
Name   : Book Name
Author : Author Name
DoP    : Date of Publish
DoR    : Date of Read
RoS    : Review of Score
*      : Key was used in sort
_      : Item you are selecting
-----------------------------------------------------------------------------------------
Command:
i/I    : sorted in ID
e/E    : sorted in Name
a/A    : sorted in Author
o/O    : sorted in DoP
r/R    : sorted in DoR
s/S    : sorted in RoS
add    : add an item
edit   : edit an item
view   : view an item
find   : find an item by Name
delete : delete an item
m      : cancel and then return to main view
p      : previous page, 20 items in a page
n      : next page, 20 items in a page
u      : up item
d      : down item
exit   : exit program
==========================================================================================      \
'''
        self.assertEqual(len(res), len(ref))
        self.assertEqual(res, ref)

    def testAddViewCorrect(self):
        av = AddEditView(self.controller, "add")
        name = "book1"
        author = "author1"
        dop = "1/3/2016"
        dor = "1/5/2016"
        ros = 1
        add = "%s\n%s\n%s\n%s\n%d" % (name, author, dop, dor, ros)
        self.controller.setInputValue(add)
        ret = av.run()
        self.assertTrue(ret)
        self.assertEqual(av.name, name)
        self.assertEqual(av.author, author)
        self.assertEqual(av.DoP, dop)
        self.assertEqual(av.DoR, dor)
        self.assertEqual(av.RoS, ros)

    def testAddViewWrong(self):
        av = AddEditView(self.controller, "add")
        name = ""
        author = "author1"
        dop = "1/3/2016"
        dor = "1/5/2016"
        ros = 1
        add = "%s\n%s\n%s\n%s\n%d" % (name, author, dop, dor, ros)
        self.controller.setInputValue(add)
        ret = av.run()
        self.assertFalse(ret)
        self.assertIsNone(av.name)
        self.assertIsNone(av.author)
        self.assertIsNone(av.DoP)
        self.assertIsNone(av.DoR)
        self.assertIsNone(av.RoS)

    def testAddViewEscape(self):
        av = AddEditView(self.controller, "add")
        name = ""
        author = "author1"
        dop = "1/3/2016"
        dor = "1/5/2016"
        ros = "m"
        add = "%s\n%s\n%s\n%s\n%s" % (name, author, dop, dor, ros)
        self.controller.setInputValue(add)
        ret = av.run()
        self.assertFalse(ret)
        self.assertIsNone(av.name)
        self.assertIsNone(av.author)
        self.assertIsNone(av.DoP)
        self.assertIsNone(av.DoR)
        self.assertIsNone(av.RoS)
        
    def testEditViewCorrect(self):
        av = AddEditView(self.controller, "edit")
        name= "d"
        author = "author1"
        dop = "1/3/2016"
        dor = "1/5/2016"
        ros = 0
        add = "%s\n%s\n%s\n%s\n%d" % (name, author, dop, dor, ros)
        self.controller.setInputValue(add)
        ret = av.run()
        self.assertTrue(ret)
        self.assertEqual(name, av.name)
        self.assertEqual(author, av.author)
        self.assertEqual(dop, av.DoP)
        self.assertEqual(dor, av.DoR)
        self.assertEqual(ros, av.RoS)

    def testEditViewWrong(self):
        av = AddEditView(self.controller, "edit")
        name = "sdfs"
        author = "author1"
        dop = "1/3/2016"
        dor = "1/5/2016"
        ros = "jfkldj"
        add = "%s\n%s\n%s\n%s\n%s" % (name, author, dop, dor, ros)
        self.controller.setInputValue(add)
        ret = av.run()
        self.assertFalse(ret)
        self.assertIsNone(av.name)
        self.assertIsNone(av.author)
        self.assertIsNone(av.DoP)
        self.assertIsNone(av.DoR)
        self.assertIsNone(av.RoS)

    def testEditViewEscape(self):
        av = AddEditView(self.controller, "add")
        name = ""
        author = "author1"
        dop = "1/3/2016"
        dor = "1/5/2016"
        ros = "m"
        add = "%s\n%s\n%s\n%s\n%s" % (name, author, dop, dor, ros)
        self.controller.setInputValue(add)
        ret = av.run()
        self.assertFalse(ret)
        self.assertIsNone(av.name)
        self.assertIsNone(av.author)
        self.assertIsNone(av.DoP)
        self.assertIsNone(av.DoR)
        self.assertIsNone(av.RoS)

    def testViewView(self):
        book = BookModel()
        book.ID = 0
        book.name = "Awesomeness!!!"
        book.author = "me"
        book.DoP = "1/3/2016"
        book.DoR = "1/7/2016"
        book.RoS = 5

        vv = ViewView(self.controller, book)
        vv.run()
        self.assertEqual(self.controller.out_file.getvalue(), "========================================================================================\nID     : 0\nName   : Awesomeness!!!\nAuthor : me\nDoP    : 1/3/2016\nDoR    : 1/7/2016\nRoS    : 5\n\n========================================================================================        ")

    def testFindView(self):
        book = BookModel()
        book.ID = 0
        book.name = "Awesomeness!!!"
        book.author = "me"
        book.DoP = "1/3/2016"
        book.DoR = "1/7/2016"
        book.RoS = 5
        self.controller.add_book(book)
        name = "Awesomeness!!!"
        fv = FindView(self.controller)
        self.controller.setInputValue(name)
        fv.run()
        self.assertEqual(self.controller.out_file.getvalue(), "Successfully found the following book\n========================================================================================\nID     : 3\nName   : Awesomeness!!!\nAuthor : me\nDoP    : 1/3/2016\nDoR    : 1/7/2016\nRoS    : 5\n\n========================================================================================        ")

if __name__ == '__main__':
    unittest.main()
