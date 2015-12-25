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
        # FIXME: fix edit/delete
        self.command_table = {"add book":self.add_book, "view book":self.view_book, "exit":self.exit_program}

    def command_handler(self, return_value):
        self.command_table[return_value]

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
        pass

    def next_page_callback(self):
        """get to the next page
        """
        pass
             
    def write(self, msg):
        self.out_file.write(msg)
        
    def readline(self):
        return self.in_file.readline()

    def add_book(self):
        av = AddView()
        av.run()
        self.mv.run()

    def add_book_callback(self, name, author, DoP, DoR, RoS):
        self.book.name = name
        self.book.author = author
        self.book.DoP = DoP
        self.book.DoR = DoR
        self.book.RoS = RoS
        self.bm.add_book(self.book)
        return self.book.ID

    def view_book(self, book_to_view):
        vv = ViewView(self, book_to_view)
        vv.run()
        self.mv.run()

    def __iter__(self):
        return self.bm.__iter__() 

    def exit_program(self):
        pass

    def run(self):
        self.mv.run()
"""
    def edit_callback(self, ID, name, author, DoP, DoR, RoS):
        del bm.books[ID]
        book = BookModel()
        book.name = name
        book.author = author
        book.DoP = DoP
        book.DoR = DoR
        book.RoS = RoS
        bm.add_book(book)
        return book.ID

    def edit_book(self):
        ev = EditView()
        ev.display()
"""
