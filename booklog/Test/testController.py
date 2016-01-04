import unittest
from Model.Model import *
from View.View import *
from Controller.Controller import *
import StringIO

class MockBookController(BookController):
    def __init__(self, in_file, out_file, db_file):
        super(MockBookController, self).__init__(in_file, out_file, db_file)
        self.inValues = ""
        self.inValuesIndex = 0

    def getvalue(self):
        ret = self.inValues[self.inValuesIndex]
        self.inValuesIndex = self.inValuesIndex + 1
        return ret

    def setInputValue(self, s):
        self.inValues = s.split('\n')
        self.inValuesIndex = 0

class ControllerTest(unittest.TestCase):
    def setUp(self):
        self.out_file = StringIO.StringIO()
        self.in_file = StringIO.StringIO()
        self.db_file = []
        self.bc = MockBookController(self.in_file, self.out_file, self.db_file)
        
#    def testMainViewController(self):
#        self.in_file.write("exit")
#        self.bc.run()
#        self.in_file.truncate(0)
#        self.assertEqual(self.bc.out_file.getvalue(), "=========================================================================================\n*ID     name                                     author          DoP        DoR        RoS \n\n-----------------------------------------------------------------------------------------\nID*    : ID, default sort in ID\nName   : Book Name\nAuthor : Author Name\nDoP    : Date of Publish\nDoR    : Date of Read\nRoS    : Review of Score\n*      : Key was used in sort\n_      : Item you are selecting\n-----------------------------------------------------------------------------------------\nCommand:\ni/I    : sorted in ID\ne/E    : sorted in Name\na/A    : sorted in Author\no/O    : sorted in DoP\nr/R    : sorted in DoR\ns/S    : sorted in RoS\nadd    : add an item\nedit   : edit an item\nview   : view an item\nfind   : find an item by Name\ndelete : delete an item\nm      : cancel and then return to main view\np      : previous page, 20 items in a page\nn      : next page, 20 items in a page\nu      : up item\nd      : down item\nexit   : exit program\n==========================================================================================      ")
#        self.bc.out_file.truncate(0)

    def testAddViewController(self):
        name = "name1"
        author = "author1"
        dop = "1/3/2016"
        dor = "1/5/2016"
        ros = 1
        add = "%s\n%s\n%s\n%s\n%s" % (name, author, dop, dor, ros)
        command = "add\n" + add + "\n" + "exit"
        self.bc.setInputValue(command)
        self.bc.run()
        res = """\
=========================================================================================
*ID     name                                     author          DoP        DoR        RoS 

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
==========================================================================================      Please input your command Please input book name(type return to skip value): Please input book author(type return to skip value): Please input book DoP(type return to skip value): Please input book DoR(type return to skip value): Please input book RoS(type return to skip value): =========================================================================================
*ID     name                                     author          DoP        DoR        RoS 
_0      name1                                    author1         1/3/2016   1/5/2016   1   

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
==========================================================================================      Please input your command """
        reta = self.out_file.getvalue().split("\n")
        resa = res.split("\n")
        self.assertEqual(len(reta), len(resa))
        for i in xrange(len(reta)):
            self.assertEqual(reta[i], resa[i])

'''

    def testEditViewController(self):
        self.bc.command_handler("edit book")
        self.in_file.truncate(0)
        self.in_file.write("exit")
        self.assertEqual(self.out_file.getvalue(), "Successfully edit the following book\n========================================================================================\nID     1\n0\n0\n0\n0\n0\n\nName   \nAuthor \nDoP    \nDoR    \nRoS    \n========================================================================================            =========================================================================================\n*ID     name                                     author          DoP        DoR        RoS \n_1      0                                        0               0          0          0   \n\n-----------------------------------------------------------------------------------------\nID*    : ID, default sort in ID\nName   : Book Name\nAuthor : Author Name\nDoP    : Date of Publish\nDoR    : Date of Read\nRoS    : Review of Score\n*      : Key was used in sort\n_      : Item you are selecting\n-----------------------------------------------------------------------------------------\nCommand:\ni/I    : sorted in ID\ne/E    : sorted in Name\na/A    : sorted in Author\no/O    : sorted in DoP\nr/R    : sorted in DoR\ns/S    : sorted in RoS\nadd    : add an item\nedit   : edit an item\nview   : view an item\nfind   : find an item by Name\ndelete : delete an item\nm      : cancel and then return to main view\np      : previous page, 20 items in a page\nn      : next page, 20 items in a page\nu      : up item\nd      : down item\nexit   : exit program\n==========================================================================================      ")
        self.bc.out_file.truncate(0)

    def testViewViewController(self):
        book = BookModel()
        book.name = "Yong"
        book.author = "Yong Liu"
        book.DoP = "12/29/2015"
        book.DoR = "12/29/2015"
        book.RoS = 5
        self.bc.bm.add_book(book)
        self.in_file.write("exit")
        self.bc.command_handler("view book")
        self.in_file.truncate(0)
        ref = "========================================================================================\nID     0\nYong\nYong Liu\n12/29/2015\n12/29/2015\n5\n\nName  \nAuthor\nDoP   \nDoR   \nRoS   \n========================================================================================        =========================================================================================\n*ID     name                                     author          DoP        DoR        RoS \n_0      Yong                                     Yong Liu        12/29/2015 12/29/2015 5   \n\n-----------------------------------------------------------------------------------------\nID*    : ID, default sort in ID\nName   : Book Name\nAuthor : Author Name\nDoP    : Date of Publish\nDoR    : Date of Read\nRoS    : Review of Score\n*      : Key was used in sort\n_      : Item you are selecting\n-----------------------------------------------------------------------------------------\nCommand:\ni/I    : sorted in ID\ne/E    : sorted in Name\na/A    : sorted in Author\no/O    : sorted in DoP\nr/R    : sorted in DoR\ns/S    : sorted in RoS\nadd    : add an item\nedit   : edit an item\nview   : view an item\nfind   : find an item by Name\ndelete : delete an item\nm      : cancel and then return to main view\np      : previous page, 20 items in a page\nn      : next page, 20 items in a page\nu      : up item\nd      : down item\nexit   : exit program\n==========================================================================================      "
        self.assertEqual(self.out_file.getvalue(), ref)
        self.bc.out_file.truncate(0)

    def testDeleteViewController(self):
        book = BookModel()
        book.name = "Yong"
        book.author = "Yong Liu"
        book.DoP = "12/29/2015"
        book.DoR = "12/29/2015"
        book.RoS = 5
        self.bc.bm.add_book(book)
        self.in_file.write("exit")
        self.bc.command_handler("delete book")
        self.in_file.truncate(0)
        self.assertEqual(self.out_file.getvalue(), "Successfully delete the following book\n========================================================================================\nID     0\nYong\nYong Liu\n12/29/2015\n12/29/2015\n5\n\nName   \nAuthor \nDoP    \nDoR    \nRoS    \n========================================================================================        =========================================================================================\n*ID     name                                     author          DoP        DoR        RoS \n\n-----------------------------------------------------------------------------------------\nID*    : ID, default sort in ID\nName   : Book Name\nAuthor : Author Name\nDoP    : Date of Publish\nDoR    : Date of Read\nRoS    : Review of Score\n*      : Key was used in sort\n_      : Item you are selecting\n-----------------------------------------------------------------------------------------\nCommand:\ni/I    : sorted in ID\ne/E    : sorted in Name\na/A    : sorted in Author\no/O    : sorted in DoP\nr/R    : sorted in DoR\ns/S    : sorted in RoS\nadd    : add an item\nedit   : edit an item\nview   : view an item\nfind   : find an item by Name\ndelete : delete an item\nm      : cancel and then return to main view\np      : previous page, 20 items in a page\nn      : next page, 20 items in a page\nu      : up item\nd      : down item\nexit   : exit program\n==========================================================================================      ")
        self.out_file.truncate(0)

    def testPageController(self):
        self.in_file.write("exit")
        self.bc.next_page_callback()
        self.bc.previous_page_callback()
        self.assertEqual(self.out_file.getvalue(), "=========================================================================================\n*ID     name                                     author          DoP        DoR        RoS \n\n-----------------------------------------------------------------------------------------\nID*    : ID, default sort in ID\nName   : Book Name\nAuthor : Author Name\nDoP    : Date of Publish\nDoR    : Date of Read\nRoS    : Review of Score\n*      : Key was used in sort\n_      : Item you are selecting\n-----------------------------------------------------------------------------------------\nCommand:\ni/I    : sorted in ID\ne/E    : sorted in Name\na/A    : sorted in Author\no/O    : sorted in DoP\nr/R    : sorted in DoR\ns/S    : sorted in RoS\nadd    : add an item\nedit   : edit an item\nview   : view an item\nfind   : find an item by Name\ndelete : delete an item\nm      : cancel and then return to main view\np      : previous page, 20 items in a page\nn      : next page, 20 items in a page\nu      : up item\nd      : down item\nexit   : exit program\n==========================================================================================      =========================================================================================\n*ID     name                                     author          DoP        DoR        RoS \n\n-----------------------------------------------------------------------------------------\nID*    : ID, default sort in ID\nName   : Book Name\nAuthor : Author Name\nDoP    : Date of Publish\nDoR    : Date of Read\nRoS    : Review of Score\n*      : Key was used in sort\n_      : Item you are selecting\n-----------------------------------------------------------------------------------------\nCommand:\ni/I    : sorted in ID\ne/E    : sorted in Name\na/A    : sorted in Author\no/O    : sorted in DoP\nr/R    : sorted in DoR\ns/S    : sorted in RoS\nadd    : add an item\nedit   : edit an item\nview   : view an item\nfind   : find an item by Name\ndelete : delete an item\nm      : cancel and then return to main view\np      : previous page, 20 items in a page\nn      : next page, 20 items in a page\nu      : up item\nd      : down item\nexit   : exit program\n==========================================================================================      ")
        self.out_file.truncate(0)
'''
