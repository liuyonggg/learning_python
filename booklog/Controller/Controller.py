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

class MainViewController(Controller):
    """controller for Main View
    """
    def __init__(self, in_file, out_file):
        self.mv = MainView(self)
        self.bm = BookManagerModel()
        self.in_file = in_file
        self.out_file = out_file

    def exit_mainview_callback(self):
        pass

    def sort_book_by_ID(self):
        """sort books by ID
        """
        self.bm.sort_book_by_ID()

    def sort_book_by_name(self):
        """sort books by name
        """
        self.bm.sort_book_by_name()

    def sort_book_by_author(self):
        """sort books by author
        """
        self.bm.sort_book_by_author()

    def sort_book_by_DoP(self):
        """sort books by DoP
        """
        self.bm.sort_book_by_DoP()

    def sort_book_by_DoR(self):
        """sort books by DoR
        """
        self.bm.sort_book_by_DoR()

    def sort_book_by_RoS(self):
        """sort books by RoS
        """
        self.bm.sort_book_by_RoS()

    def add_callback(self):
        """add a book
        """
        pass

    def edit_callback(self):
        """edit a book
        """
        pass

    def previous_page_callback(self):
        """get to the previous page
        """
        pass

    def next_page_callback(self):
        """get to the next page
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
    
    def run(self): 
        self.mv.display()
        self.mv.handler()
