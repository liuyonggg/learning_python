'''
Copyright (c) <2015> Zechen Liu
    
    

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:



The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.



THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

class View(object):
    """class for View
    """
    def handler(self, controller):
        """ handler
        Return:
            view
        """
        return self

class MainView(View):
    """class for MainView
    """
    def __init__(self, controller):
        self.numberBooks = 20
        self.headers_title = ["ID", "name", "author", "DoP", "DoR",  "RoS"]
        self.headers_width = [5,  40, 15,  10,  10, 3]
        self.headers_type  = ["d",  "s", "s",  "s",  "s", "d"]
        self.sort_index = 0
        self.bookFormat = ""
        for i in xrange(len(self.headers_title)):
            self.bookFormat = self.bookFormat + "%(" + self.headers_title[i] + ")-" + "%d" % (self.headers_width[i]) + self.headers_type[i]
        self.controller = controller
        self.commandTable = {"i":self.on_sort_by_ID_handler, "add":self.on_add_handler, "view":self.on_view_handler, "u":self.on_up_handler, "exit":self.on_exit_handler}
        self.bookIndex = 0
        self.books = []
        # FIXME: should move out m: return to main view
        self.format = """\
========================================================================================
%(headers)s
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

    def load_books(self):
        """load books from contoller
        """
        i = 0
        self.books = []
        self.bookIndex = 0
        for book in self.controller:
            # FIXME: should handle previous page and next page
            if i == self.numberBooks:
                break
            i = i + 1
            self.books.append(book)


    def display(self):
        """display 
        Return:
            view
        """
        headers = ""
        for i in xrange(len(self.headers_title)):
            f = "%%-%ds" % self.headers_width[i]
            headers = headers + f % self.headers_title[i] if i != self.sort_index else  headers + f % (self.headers_title[i] + "*")
        books = ""
        i = 0
        for book in self.books:
            if i == self.bookIndex:
                books = books + "*" + self.bookFormat %  {"ID": book.ID,"name":book.name, "author":book.author, "DoP":book.DoP, "DoR":book.DoR, "RoS":book.RoS} + "\n"
            else:
                books = books + " " + self.bookFormat %  {"ID": book.ID,"name":book.name, "author":book.author, "DoP":book.DoP, "DoR":book.DoR, "RoS":book.RoS} + "\n"
            i = i + 1
        self.controller.write(self.format % {"books": books, "headers": headers})

    def handler(self):
        """all command handler
        Return:
            view
        """
        while True:
            command = self.controller.readline().lower()
            self.commandTable[command]()
            if command == "exit":
                break
        self.controller.exit_mainview_callback()
    
    def on_sort_by_ID_handler(self):
        """sort ID command handler
        """
        self.sort_index = 0
        self.controller.sort_by_ID_callback()
        self.display()

    def on_add_handler(self):
        """add command handler
        """
        self.controller.add_callback()
        self.display()

    def on_view_handler(self):
        """view command handler
        """
        self.controller.view_callback(self.bookID)


    def on_up_handler(self):
        """up command handler
        """
        self.bookIndex = self.bookIndex + 1 if self.bookIndex < len(self.books) else self.bookIndex


    def on_exit_handler(self):
        """exit command handler
        """
        pass
