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
        self.db_file = db_file
        self.command_table = {"add book":self.add_book, "edit book":self.edit_book, "view book":self.view_book, "exit":self.exit_program, "delete book":self.delete_book, "find book":self.find_book}
        if self.db_file:
            s = "".join(self.db_file.readlines())
            self.bm.deserialize(s)
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
        if self.number_books - MainView.booksInAPage >= 0:
            self.number_books -= MainView.booksInAPage
        self.mv.load_books()
        self.mv.display()

    def next_page_callback(self):
        """get to the next page
        """
        if self.number_books + MainView.booksInAPage < len(self.bm.books):
            self.number_books += MainView.booksInAPage
        self.mv.load_books()
        self.mv.display()

    def write(self, msg):
        self.out_file.write(msg)
        
    def getvalue(self):
        return self.in_file.getvalue().strip()

    def add_book(self):
        av = AddEditView(self, "add")
        if av.run():
            book = BookModel()
            book.name = av.name
            book.author = av.author
            book.DoP = av.DoP
            book.DoR = av.DoR
            book.RoS = av.RoS
            self.bm.add_book(book)
        self.mv.load_books()
        self.mv.display()

    def validate_book(self, type, name, author, DoP, DoR, RoS):
        if type == "add":
            return name and author and DoP and DoR and RoS != None and RoS.isdigit()
        elif type == "edit":
            return RoS.isdigit()

    def view_book(self):
        vv = ViewView(self, self.bm.books[self.mv.book_index])
        vv.run()
        self.mv.display()

    def __iter__(self):
        self.bm.change_starting_index(self.number_books)
        return self.bm.__iter__() 

    def exit_program(self):
        if self.db_file and isinstance(self.db_file, file):
            self.db_file.truncate(0)
            self.db_file.seek(0)
            s = self.bm.serialize()
            self.db_file.write(s)

    def run(self):
        return self.mv.run()

    def edit_book(self):
        ev = AddEditView(self, "edit")
        ev.run()
        book = self.bm.books[self.mv.book_index]
        if ev.name:
            book.name = ev.name
        if ev.author:
            book.author = ev.author
        if ev.DoP:
            book.DoP = ev.DoP
        if ev.DoR:
            book.DoR = ev.DoR
        if ev.RoS >= 0:
            book.RoS = ev.RoS
        self.mv.load_books()
        self.mv.display()

    def delete_book(self):
        if self.mv.book_index < len(self.bm.books):
            del self.bm.books[self.mv.book_index]
        else:
            self.write("You need to add a book in order to delete!")

        self.mv.load_books()
        self.mv.display()

    def find_book(self):
        fv = FindView(self)
        fv.run()
        self.mv.display()

    def find_callback(self, name):
        return self.bm.search_book_by_name(name)
