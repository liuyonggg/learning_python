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
    def display(self, model):
        """ display 
        Return:
            view
        """
        return self

class MainView(View):
    """class for MainView
    """
    def __init__(self):
        self.numberBooks = 20
        self.bookFormat = "%(ID)-5d  %(name)-40s %(author)-15s %(DoP)-10s %(DoR)-10s %(RoS)-3d"
        self.format = """\
========================================================================================
ID     Name                                    Author          DoP        DoR        RoS
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
exit  : exit program
========================================================================================\
        """
    
    def display(self, model):
        """display
        Return:
            view
        """
        books = ""
        i = 0
        for book in model:
            if i == self.numberBooks:
                break
            books = books + self.bookFormat %  {"ID": book.ID,    "name":book.name, "author":book.author, "DoP":book.DoP, "DoR":book.DoR, "RoS":book.RoS} + "\n"
            i = i + 1
        print self.format % {"books": books}
        return self
