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

    def write(self, msg):
        self.out_file.write(msg)
        
    def getvalue(self):
        ret = self.inValues[self.inValuesIndex]
        self.inValuesIndex = self.inValuesIndex + 1
        return ret

    def __iter__(self):
        return self.bm.__iter__(0)

    def run(self):
        self.mv.display()
        self.mv.handler()

    def setInputValue(self, s):
        self.inValues = s.split('\n')
        self.inValuesIndex = 0

    def validate_book(self, name, author, DoP, DoR, RoS):
        return name and author and DoP and DoR and RoS and RoS.isdigit()

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
        ref = "=========================================================================================\n*ID     name                                     author          DoP        DoR        RoS \n_0      weirdo                                   Bob             2004-7-7   2005-6-7   0   \n 1      zeirdo                                   Job             2007-7-7   2009-6-7   5   \n 2      zeirdo                                   Job             2007-7-7   2009-6-7   5   \n\n-----------------------------------------------------------------------------------------\nID*    : ID, default sort in ID\nName   : Book Name\nAuthor : Author Name\nDoP    : Date of Publish\nDoR    : Date of Read\nRoS    : Review of Score\n*      : Key was used in sort\n_      : Item you are selecting\n-----------------------------------------------------------------------------------------\nCommand:\ni/I    : sorted in ID\ne/E    : sorted in Name\na/A    : sorted in Author\no/O    : sorted in DoP\nr/R    : sorted in DoR\ns/S    : sorted in RoS\nadd    : add an item\nedit   : edit an item\nview   : view an item\nfind   : find an item by Name\ndelete : delete an item\nm      : cancel and then return to main view\np      : previous page, 20 items in a page\nn      : next page, 20 items in a page\nu      : up item\nd      : down item\nexit   : exit program\n==========================================================================================      "
        self.assertEqual(len(res), len(ref))
        self.assertEqual(res, ref)

    def testAddViewCorrect(self):
        av = AddView(self.controller)
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
        av = AddView(self.controller)
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
        av = AddView(self.controller)
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
        

if __name__ == '__main__':
    unittest.main()
