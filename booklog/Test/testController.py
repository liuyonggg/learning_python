import unittest
from Model.Model import *
from View.View import *
from Controller.Controller import *
import StringIO

class ControllerTest(unittest.TestCase):
    def setUp(self):
        self.out_file = StringIO.StringIO()
        self.in_file = StringIO.StringIO()
        self.db_file = []
        self.bc = BookController(self.in_file, self.out_file, self.db_file)
        
'''
    def testMainViewController(self):
        self.in_file.write("exit")
        self.bc.run()
        self.in_file.truncate(0)
        self.assertEqual(self.bc.out_file.getvalue(), "=========================================================================================\n*ID     name                                     author          DoP        DoR        RoS \n\n-----------------------------------------------------------------------------------------\nID*    : ID, default sort in ID\nName   : Book Name\nAuthor : Author Name\nDoP    : Date of Publish\nDoR    : Date of Read\nRoS    : Review of Score\n*      : Key was used in sort\n_      : Item you are selecting\n-----------------------------------------------------------------------------------------\nCommand:\ni/I    : sorted in ID\ne/E    : sorted in Name\na/A    : sorted in Author\no/O    : sorted in DoP\nr/R    : sorted in DoR\ns/S    : sorted in RoS\nadd    : add an item\nedit   : edit an item\nview   : view an item\nfind   : find an item by Name\ndelete : delete an item\nm      : cancel and then return to main view\np      : previous page, 20 items in a page\nn      : next page, 20 items in a page\nu      : up item\nd      : down item\nexit   : exit program\n==========================================================================================      ")
        self.bc.out_file.truncate(0)

    def testAddViewController(self):
        self.in_file.write("exit")
        self.bc.command_handler("add book")
        self.in_file.truncate(0)
        self.assertEqual(self.out_file.getvalue(), "========================================================================================\nID     0\n0\n0\n0\n0\n0\n\nName   \nAuthor \nDoP    \nDoR    \nRoS    \n========================================================================================        =========================================================================================\n*ID     name                                     author          DoP        DoR        RoS \n_0      0                                        0               0          0          0   \n\n-----------------------------------------------------------------------------------------\nID*    : ID, default sort in ID\nName   : Book Name\nAuthor : Author Name\nDoP    : Date of Publish\nDoR    : Date of Read\nRoS    : Review of Score\n*      : Key was used in sort\n_      : Item you are selecting\n-----------------------------------------------------------------------------------------\nCommand:\ni/I    : sorted in ID\ne/E    : sorted in Name\na/A    : sorted in Author\no/O    : sorted in DoP\nr/R    : sorted in DoR\ns/S    : sorted in RoS\nadd    : add an item\nedit   : edit an item\nview   : view an item\nfind   : find an item by Name\ndelete : delete an item\nm      : cancel and then return to main view\np      : previous page, 20 items in a page\nn      : next page, 20 items in a page\nu      : up item\nd      : down item\nexit   : exit program\n==========================================================================================      ")
        self.bc.out_file.truncate(0)

    def testEditViewController(self):
        self.in_file.write("exit")
        self.bc.command_handler("edit book")
        self.in_file.truncate(0)
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
