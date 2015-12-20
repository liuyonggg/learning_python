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
        self.command_table = {"i":self.on_sort_book_by_ID_handler, "add":self.on_add_book_handler, "view":self.on_view_handler, "exit":self.on_exit_handler, "u":self.on_up_handler, "p":self.on_previous_page_handler}
        self.book_index = 0
        self.bookFormat = ""
        for i in xrange(len(self.headers_title)):
            self.bookFormat = self.bookFormat + "%%(%s)-%d%s" % (self.headers_title[i], self.headers_width[i], self.headers_type[i])
        self.format = """\
=========================================================================================
%(headers)s
%(books)s
-----------------------------------------------------------------------------------------
ID*   : ID, default sort in ID
Name  : Book Name
Author: Author Name
DoP   : Date of Publish
DoR   : Date of Read
RoS   : Review of Score
*     : Key was used in sort
_     : Item you are selecting
-----------------------------------------------------------------------------------------
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
=========================================================================================\
        """

    def load_books(self):
        #FIXME: Should handle previous and next page
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

    def handler(self):
        while True:
            command = raw_input("Enter your command. ")
            if command not in self.command_table:
                print "Opps!!!, that is an invalid command."
            else:
                self.command_table[command.lower()]
                if command == "exit":
                    break

    def on_sort_book_by_ID_handler(self):
        self.sort_index = 0
        self.controller.sort_book_by_ID()
        self.load_books()
        self.display()

    def on_add_book_handler(self):
        self.controller.add_callback()

    def on_view_handler(self):
        self.controller.view_callback(self.books[self.book_index])

    def on_exit_handler(self):
        self.controller.exit_mainview_callback()

    def on_up_handler(self):
        if self.book_index > 0:
            self.book_index -= 1
            self.display()

    def on_previous_page_handler(self):
        self.controller.previous_page_callback()

Class AddView(View):
    def __init__(self, controller):
        self.controller = controller
        self.name = raw_input("Please input book name(type return to skip or keep original value: )")
        self.author = raw_input("Please input book author(type return to skip or keep original value: )")
        self.DoP = raw_input("Please input Date of Publish(type return to skip or keep original value: ))")
        self.DoR = raw_input("Please input Date of Read(type return to skip or keep original value: )")
        self.RoS = raw_input("Please input Review of Score(0 - 5)(type return to skip or keep original value: )")
        self.format = """\
========================================================================================
%(headers)s %(book)s
========================================================================================\
        """
        self.headers = "ID\nName\nAuthor\nDoP\nDoR\nRoS\n"

    def display(self):
