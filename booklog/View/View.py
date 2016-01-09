import StringIO
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
    """class for view
    """
    def handler(self, controller):
        """handler
        Return:
            View
        """
        return self

class MainView(View):
    booksInAPage = 20
    def __init__(self, controller):
        self.books = []
        self.sort_index = 0
        self.controller = controller
        self.booksInAPage = MainView.booksInAPage
        self.headers_title = ["ID", "name", "author", "DoP", "DoR", "RoS"]
        self.headers_width = [7, 41, 16, 11, 11, 4]
        self.headers_type = ["s", "s", "s", "s", "s", "s"]
        self.command_table = {"i":self.on_sort_book_by_ID_handler, "e":self.on_sort_book_by_name_handler, "a":self.on_sort_book_by_author_handler, "o":self.on_sort_book_by_DoP_handler, "r":self.on_sort_book_by_DoR_handler, "s":self.on_sort_book_by_RoS_handler, "add":self.on_add_book_handler, "edit":self.on_edit_handler, "view":self.on_view_handler, "find":self.on_find_handler, "delete":self.on_delete_handler, "p":self.on_previous_page_handler, "n":self.on_next_page_handler, "u":self.on_up_handler, "d":self.on_down_handler, "exit":self.on_exit_handler}
        self.book_index = 0
        self.bookFormat = ""
        for i in xrange(len(self.headers_title)):
            self.bookFormat = self.bookFormat + "%%(%s)-%d%s" % (self.headers_title[i], self.headers_width[i], self.headers_type[i])
        self.format = """\
=========================================================================================
%(headers)s
%(books)s
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
==========================================================================================\
      """

    def load_books(self):
        i = 0
        self.books = []
        for book in self.controller:
            if i < self.booksInAPage:
                self.books.append(book)
                i += 1
            else:
                assert(i == self.booksInAPage)
                break
        return self.books

    def display(self):
        self.headers = ""
        f = "%%(%s)-%d%s"
        for i in xrange(len(self.headers_title)):
            if i == self.sort_index:
                self.headers = self.headers + "*" + f % (self.headers_title[i], self.headers_width[i]-1, self.headers_type[i]) % {self.headers_title[i]:self.headers_title[i]}
            else:
                self.headers = self.headers + f % (self.headers_title[i], self.headers_width[i], self.headers_type[i]) % {self.headers_title[i]: self.headers_title[i]}
        i = 0
        books = ""
        for book in self.books:
            if self.book_index == i:
                books = books + self.bookFormat % {"ID":"_%s" % book.ID, "name":book.name if len(book.name) < 42 else book.name[:41], "author":book.author if len(book.author) < 17 else book.name[:16], "DoP":book.DoP if len(book.DoP) < 12 else book.DoP[:11], "DoR":book.DoR if len(book.DoR) < 12 else book.DoR[:11], "RoS":book.RoS} + "\n"
            else:
                books = books + self.bookFormat % {"ID":" %s" % book.ID, "name":book.name if len(book.name) <= self.headers_width[1] else book.name[:self.headers_width[1]], "author":book.author if len(book.author) < 17 else book.name[:16], "DoP":book.DoP if len(book.DoP) < 12 else book.DoP[:11], "DoR":book.DoR if len(book.DoR) < 12 else book.DoR[:11], "RoS":book.RoS} + "\n"
            i += 1
        self.controller.write(self.format % {"headers":self.headers, "books":books})

    def handler(self):
        while True:
            self.controller.write("Please input your command ")
            command = self.controller.getvalue().lower()
            if command not in self.command_table:
                self.controller.write("Opps!!!, that is an invalid command.")
            else:
                self.command_table[command.lower()]()
                if command == "exit":
                    break

    def on_sort_book_by_ID_handler(self):
        self.sort_index = 0
        self.controller.sort_book_by_ID_callback()
        self.load_books()
        self.display()

    def on_sort_book_by_name_handler(self):
        self.sort_index = 1
        self.controller.sort_book_by_name_callback()
        self.load_books()
        self.display()

    def on_sort_book_by_author_handler(self):
        self.sort_index = 2
        self.controller.sort_book_by_author_callback()
        self.load_books()
        self.display()

    def on_sort_book_by_DoP_handler(self):
        self.sort_index = 3
        self.controller.sort_book_by_DoP_callback()
        self.load_books()
        self.display()

    def on_sort_book_by_DoR_handler(self):
        self.sort_index = 4
        self.controller.sort_book_by_DoR_callback()
        self.load_books()
        self.display()

    def on_sort_book_by_RoS_handler(self):
        self.sort_index = 5
        self.controller.sort_book_by_RoS_callback()
        self.load_books()
        self.display()

    def on_add_book_handler(self):
        self.controller.command_handler("add book")

    def on_edit_handler(self):
        self.controller.command_handler("edit book")

    def on_view_handler(self):
        self.controller.command_handler("view book")

    def on_find_handler(self):
        self.controller.command_handler("find book")

    def on_delete_handler(self):
        self.controller.command_handler("delete book")

    def on_previous_page_handler(self):
        self.controller.previous_page_callback()

    def on_next_page_handler(self):
        self.controller.next_page_callback()

    def on_up_handler(self):
        if self.book_index > 0:
            self.book_index -= 1
            self.display()

    def on_down_handler(self):
        if self.book_index < len(self.books)-1:
            self.book_index += 1
            self.display()

    def on_exit_handler(self):
        self.controller.command_handler("exit")

    def run(self):
        self.load_books()
        self.display()
        self.handler()

class AddEditView(View):
    def __init__(self, controller, type):
        self.controller = controller
        self.name = None
        self.author = None
        self.DoP = None
        self.DoR = None
        self.RoS = None
        self.type = type
 
    def display(self, prompt):
        self.controller.write(prompt)

    def run(self):
        expectInput = ["book name", "book author", "book DoP", "book DoR", "book RoS"]
        expectInputValue = []
        if self.type == "add":
            for i in xrange(len(expectInput)):
                self.display("Please input %s(type return to skip value): " % expectInput[i])
                s = self.controller.getvalue()
                if s == 'm':
                    return False
                expectInputValue.append(s)
            ## FIXME: need give prompt for wrong input
            if not self.controller.validate_book(self.type, *expectInputValue):
                ## self.display("can't add the book, input is not valid")
                return False

        elif self.type == "edit":
            for i in xrange(len(expectInput)):
                self.display("Please input %s(type return to keep original value): " % expectInput[i])
                s = self.controller.getvalue()
                if s == 'm':
                    return False
                expectInputValue.append(s)
            ## FIXME: need give prompt for wrong input
            if not self.controller.validate_book(self.type, *expectInputValue):
                ## self.display("can't edit the book, input is not valid")
                return False

        self.name = expectInputValue[0]
        self.author = expectInputValue[1]
        self.DoP = expectInputValue[2]
        self.DoR = expectInputValue[3]
        self.RoS = int(expectInputValue[4])
        return True

class ViewView(View):
    def __init__(self, controller, book):
        self.controller = controller
        self.book_format = ""
        self.book = book
        self.ID = book.ID
        self.name = book.name
        self.author = book.author
        self.DoP = book.DoP
        self.DoR = book.DoR
        self.RoS = book.RoS
        self.format = """\
========================================================================================
%(book)s
========================================================================================\
        """
        headers = ["ID", "Name", "Author", "DoP", "DoR", "RoS"]
        for i in xrange(len(headers)):
            self.book_format += "%-7s: %%(%s)s\n" % (headers[i], headers[i])

    def display(self):
        book = self.book_format % {"ID":self.ID, "Name":self.name, "Author":self.author, "DoP":self.DoP, "DoR":self.DoR, "RoS":self.RoS}
        self.controller.write(self.format % {"book":book})

    def run(self):
        self.display()

class FindView(View):
    def __init__(self, controller):
        self.controller = controller
        self.book_format = ""
        self.headers = ""
        self.format = """\
Successfully found the following book
========================================================================================
%(book)s
========================================================================================\
        """
        headers = ["ID", "Name", "Author", "DoP", "DoR", "RoS"]
        for i in xrange(len(headers)):
            self.book_format = self.book_format + "%-7s: %%(%s)s\n" % (headers[i], headers[i])

    def display(self):
        if self.book != None:
            self.book = self.book_format % {"ID":self.ID, "Name":self.name, "Author":self.author, "DoP":self.DoP, "DoR":self.DoR, "RoS":self.RoS}
            self.controller.write(self.format % {"book":self.book})

        else:
            self.controller.write("There is no book with the name of %s"%self.name)

    def run(self):
        self.name = self.controller.getvalue()
        if self.name == "m":
            self.controller.run()
        self.book = self.controller.find_callback(self.name)
        if self.book != None:
            self.ID = self.book.ID
            self.name = self.book.name
            self.author = self.book.author
            self.DoP = self.book.DoP
            self.DoR = self.book.DoR
            self.RoS = self.book.RoS
        self.display()
