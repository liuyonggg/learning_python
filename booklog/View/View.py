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
    def __init__(self, controller):
        self.books = []
        self.sort_index = 0
        self.controller = controller
        self.booksInAPage = 20
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
                self.headers = self.headers + "*" + f % (self.headers_title[i], self.headers_width[i], self.headers_type[i]) % {self.headers_title[i]:self.headers_title[i]}
            else:
                self.headers = self.headers + f % (self.headers_title[i], self.headers_width[i], self.headers_type[i]) % {self.headers_title[i]: self.headers_title[i]}
        i = 0
        books = ""
        for book in self.books:
            if self.book_index == i:
                books = books + self.bookFormat % {"ID":"_%-7d"%book.ID, "name":book.name if len(book.name) < 42 else book.name[:41], "author":book.author if len(book.author) < 17 else book.name[:16], "DoP":book.DoP if len(book.DoP) < 12 else book.DoP[:11], "DoR":book.DoR if len(book.DoR) < 12 else book.DoR[:11], "RoS":book.RoS} + "\n"
            else:
                books = books + self.bookFormat % {"ID":" %-7d"%book.ID, "name":book.name if len(book.name) < 42 else book.name[:41], "author":book.author if len(book.author) < 17 else book.name[:16], "DoP":book.DoP if len(book.DoP) < 12 else book.DoP[:11], "DoR":book.DoR if len(book.DoR) < 12 else book.DoR[:11], "RoS":book.RoS} + "\n"
            i += 1
        self.controller.write(self.format % {"headers":self.headers, "books":books})
        print self.format % {"headers":self.headers, "books":books}

    def handler(self):
        while True:
            command = raw_input("Please input your command ")
            if command not in self.command_table:
                print "Opps!!!, that is an invalid command."
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

class AddView(View):
    def __init__(self, controller):
        self.controller = controller
        self.book_format = ""
        self.format = """\
========================================================================================
%(book)s
========================================================================================\
        """
        headers = ["ID", "Name", "Author", "DoP", "DoR", "RoS"]
        for i in xrange(len(headers)):
            self.book_format += "%-7s: %%(%s)s\n" % (headers[i], headers[i])

    def display(self):
        self.name = raw_input("Please input book name(type return to skip or keep original value: )")
        if self.name == "m":
            self.controller.run()

        self.author = raw_input("Please input book author(type return to skip or keep original value: )")
        if self.author == "m":
            self.controller.run()

        self.DoP = raw_input("Please input Date of Publish(type return to skip or keep original value: )")
        if self.DoP == "m":
            self.controller.run()

        self.DoR = raw_input("Please input Date of Read(type return to skip or keep original value: )")
        if self.DoR == "m":
            self.controller.run()

        self.RoS = raw_input("Please input Review of Score(0 - 5)(type return to skip or keep original value: )")
        if self.RoS == "m":
            self.controller.run()

        if not self.name:
            self.name = "None"
        if not self.author:
            self.author = "None"
        if not self.DoP:
            self.DoP = "None"
        if not self.DoR:
            self.DoR = "None"
        if not self.RoS:
            self.RoS = "None"
        self.ID = self.controller.add_book_callback(self.name, self.author, self.DoP, self.DoR, self.RoS)

        book = self.book_format % {"ID":self.ID, "Name":self.name, "Author":self.author, "DoP":self.DoP, "DoR":self.DoR, "RoS":self.RoS}
        self.controller.write(self.format % {"book":book})
        print self.format % {"book":book}

    def run(self):
        self.display()

class EditView(View):
    def __init__(self, controller):
        self.book_format = ""
        self.controller = controller
        self.format = """\
Successfully edit the following book
========================================================================================
%(book)s
========================================================================================\
            """
        headers = ["ID", "Name", "Author", "DoP", "DoR", "RoS"]
        for i in xrange(len(headers)):
            self.book_format = self.book_format + "%-7s: %%(%s)s\n" % (headers[i], headers[i])

    def display(self):
        self.ID = raw_input("Please input ID of the book you want to edit: ")
        if self.ID == "m":
            self.controller.run()

        self.name = raw_input("Please input new book name(type return to skip or keep original value): ")
        if self.name == "m":
            self.controller.run()

        self.author = raw_input("Please input new book author(type return to skip or keep original value): ")
        if self.author == "m":
            self.controller.run()

        self.DoP = raw_input("Please input new book DoP(type return to skip or keep original value): ")
        if self.DoP == "m":
            self.controller.run()

        self.DoR = raw_input("Please input new book DoR(type return to skip or keep original value): ")
        if self.DoR == "m":
            self.controller.run()

        self.RoS = raw_input("Please input new book RoS(0 - 5)(type return to skip or keep original value): ")
        if self.RoS == "m":
            self.controller.run()

        if not self.name:
            self.name = "None"
        if not self.author:
            self.author = "None"
        if not self.DoP:
            self.DoP = "None"
        if not self.DoR:
            self.DoR = "None"
        if self.RoS == "":
            self.RoS = "None"

        self.ID = self.controller.edit_callback(self.ID, self.name, self.author, self.DoP, self.DoR, self.RoS)

        book = self.book_format % {"ID":self.ID, "Name":self.name, "Author":self.author, "DoP":self.DoP, "DoR":self.DoR, "RoS":self.RoS}
        self.controller.write(self.format % {"book":book})
        print self.format % {"book":book}

    def run(self):
        self.display()

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
        print self.format % {"book":book}

    def run(self):
        self.display()

class DeleteView(View):
    def __init__(self, controller, book):
        self.controller = controller
        self.ID = book.ID
        self.name = book.name
        self.author = book.author
        self.DoP = book.DoP
        self.DoR = book.DoR
        self.RoS = book.RoS
        self.book_format = ""
        self.format = """\
Successfully delete the following book
========================================================================================
%(book)s
========================================================================================\
        """
        headers = ["ID", "Author", "Author", "DoP", "DoR", "RoS"]
        for i in xrange(6):
            self.book_format += "%-7s: %%(%s)s\n" % (headers[i], headers[i])

    def display(self):
        book = self.book_format % {"ID":self.ID, "Name":self.name, "Author":self.author, "DoP":self.DoP, "DoR":self.DoR, "RoS":self.RoS}
        self.controller.write(self.format % {"book":book})
        print self.format % {"book":book}

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
        name = raw_input("Please input the name of the book you want to edit: ")
        if name == "m":
            self.controller.run()
        book = self.controller.find_callback(name)
        if book != None:
            ID = book.ID
            name = book.name
            author = book.author
            DoP = book.DoP
            DoR = book.DoR
            RoS = book.RoS

            book = self.book_format % {"ID":ID, "Name":name, "Author":author, "DoP":DoP, "DoR":DoR, "RoS":RoS}
            self.controller.write(self.format % {"book":book})
            print self.format % {"book":book}

        else:
            self.controller.write("There is no book with the name of %s"%name)
            print "There is no book with the name of", name

    def run(self):
        self.display()
