"""
Copyright (c) <2015> Zechen Liu



Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:



The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.



THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.


"""

from Model.Model import *
from View.View import *
from StringIO import *

class Controller(object):
    """controller
    """
    pass

class BookController(Controller):
    """controller for Main View
    """
    def __init__(self, in_file, out_file, db_file):
        self.mv = MainView(self)
        self.bm = BookManagerModel()
        self.in_file = in_file
        self.out_file = out_file
        self.book = BookModel()
        self.command_table = {"add book":self.add_book, "edit book":self.edit_book, "view book":self.view_book, "exit":self.exit_program, "delete book":self.delete_book, "find book":self.find_book}
        self.number_books = 0

    def command_handler(self, return_value):
        self.command_table[return_value]()

    def sort_book_by_ID_callback(self):
        """sort books by ID
        """
        self.bm.sort_book_by_ID()

    def sort_book_by_name_callback(self):
        """sort books by name
        """
        self.bm.sort_book_by_name()

    def sort_book_by_author_callback(self):
        """sort books by author
        """
        self.bm.sort_book_by_author()

    def sort_book_by_DoP_callback(self):
        """sort books by DoP
        """
        self.bm.sort_book_by_DoP()

    def sort_book_by_DoR_callback(self):
        """sort books by DoR
        """
        self.bm.sort_book_by_DoR()

    def sort_book_by_RoS_callback(self):
        """sort books by RoS
        """
        self.bm.sort_book_by_RoS()

    def previous_page_callback(self):
        """get to the previous page
        """
        if self.number_books > 0:
            self.number_books -= 20
        self.mv.run()

    def next_page_callback(self):
        """get to the next page
        """
        remainder = len(self.bm.books) - 1 % 20
        if self.number_books < len(self.bm.books)-1-remainder:
            self.number_books += 20
        self.mv.run()
             
    def write(self, msg):
        self.out_file.write(msg)
        
    def getvalue(self):
        return self.in_file.getvalue()

    def add_book(self):
        av = AddView(self, "add")
        if av.run():
            book = BookModel()
            book.name = av.name
            book.author = av.author
            book.DoP = av.DoP
            book.DoR = av.DoR
            book.RoS = av.RoS
            bm.add_book(book)
        self.mv.run()

    def validate_book(self, name, author, DoP, DoR, RoS):
        return name and author and DoP and DoR and RoS and RoS.isdigit()

    def view_book(self):
        vv = ViewView(self, self.bm.books[self.mv.book_index])
        vv.run()
        self.mv.run()

    def __iter__(self):
        return self.bm.__iter__(self.number_books) 

    def exit_program(self):
        return self.bm.serialize()

    def run(self):
        self.mv.run()

    def edit_callback(self, ID, name, author, DoP, DoR, RoS):
        b1 = BookModel()
        b2 = BookModel()
        
        ID = int(ID)
        b1 = self.bm.books[ID]
        
        if name == "None":
            name = b1.name
        if author == "None":
            author = b1.author
        if DoP == "None":
            DoP = b1.DoP
        if DoR == "None":
            DoR = b1.DoR
        if RoS == "None":
            RoS == b1.RoS

        del self.bm.books[ID]
        b2.name = name
        b2.author = author
        b2.DoP = DoP
        b2.DoR = DoR
        b2.RoS = RoS

        self.bm.add_book(b2)
        return b2.ID

    def edit_book(self):
        ev = EditView(self)
        ev.run()
        self.mv.run()

    def delete_book(self):
        del self.bm.books[self.mv.book_index]
        self.mv.run()

    def find_book(self):
        fv = FindView(self)
        fv.run()
        self.mv.run()

    def find_callback(self, name):
        return self.bm.search_book_by_name(name)
