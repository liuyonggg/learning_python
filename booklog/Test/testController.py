import unittest
from Model.Model import *
from View.View import *
from Controller.Controller import *
import StringIO

class MockBookController(BookController):
    def __init__(self, in_file, out_file, db_file):
        super(MockBookController, self).__init__(in_file, out_file, db_file)
        self.inValues = ""
        self.inValuesIndex = 0

    def getvalue(self):
        ret = self.inValues[self.inValuesIndex]
        self.inValuesIndex = self.inValuesIndex + 1
        return ret

    def setInputValue(self, s):
        self.inValues = s.split('\n')
        self.inValuesIndex = 0

class ControllerTest(unittest.TestCase):
    def setUp(self):
        self.out_file = StringIO.StringIO()
        self.in_file = StringIO.StringIO()
        self.db_file = []
        self.bc = MockBookController(self.in_file, self.out_file, self.db_file)

    def testWholeController(self):
        for i in xrange(40):
            book = BookModel()
            book.name = "name_%d" % i
            book.author = "author_%d" % i
            book.DoP = "12/29/2015"
            book.DoR = "12/29/2015"
            book.RoS = 5
            self.bc.bm.add_book(book)
        name = "name_add"
        author = "author_add"
        DoP = "2/3/2014"
        DoR = "3/5/2013"
        RoS = 5
        add = "%s\n%s\n%s\n%s\n%d\n" % (name, author, DoP, DoR, RoS)

        namee = "name_edit"
        authore = "author_edit"
        DoRe = "3/4/2013"
        DoPe = "3/4/2015"
        RoSe = 0
        edit = "%s\n%s\n%s\n%s\n%d\n" % (namee, authore, DoPe, DoRe, RoSe)
        command = "E\nA\nO\nI\nR\nS\nadd\n" + add + "edit\n" + edit + "view\nfind\nname_35\ndelete\nadd\nm\nn\np\nd\nu\nexit"
        self.bc.setInputValue(command)
        self.bc.run()
        ref = """\
=========================================================================================
*ID    name                                     author          DoP        DoR        RoS 
_0     name_0                                   author_0        12/29/2015 12/29/2015 5   
 1     name_1                                   author_1        12/29/2015 12/29/2015 5   
 2     name_2                                   author_2        12/29/2015 12/29/2015 5   
 3     name_3                                   author_3        12/29/2015 12/29/2015 5   
 4     name_4                                   author_4        12/29/2015 12/29/2015 5   
 5     name_5                                   author_5        12/29/2015 12/29/2015 5   
 6     name_6                                   author_6        12/29/2015 12/29/2015 5   
 7     name_7                                   author_7        12/29/2015 12/29/2015 5   
 8     name_8                                   author_8        12/29/2015 12/29/2015 5   
 9     name_9                                   author_9        12/29/2015 12/29/2015 5   
 10    name_10                                  author_10       12/29/2015 12/29/2015 5   
 11    name_11                                  author_11       12/29/2015 12/29/2015 5   
 12    name_12                                  author_12       12/29/2015 12/29/2015 5   
 13    name_13                                  author_13       12/29/2015 12/29/2015 5   
 14    name_14                                  author_14       12/29/2015 12/29/2015 5   
 15    name_15                                  author_15       12/29/2015 12/29/2015 5   
 16    name_16                                  author_16       12/29/2015 12/29/2015 5   
 17    name_17                                  author_17       12/29/2015 12/29/2015 5   
 18    name_18                                  author_18       12/29/2015 12/29/2015 5   
 19    name_19                                  author_19       12/29/2015 12/29/2015 5   

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
==========================================================================================      Please input your command =========================================================================================
ID     *name                                    author          DoP        DoR        RoS 
_0     name_0                                   author_0        12/29/2015 12/29/2015 5   
 1     name_1                                   author_1        12/29/2015 12/29/2015 5   
 10    name_10                                  author_10       12/29/2015 12/29/2015 5   
 11    name_11                                  author_11       12/29/2015 12/29/2015 5   
 12    name_12                                  author_12       12/29/2015 12/29/2015 5   
 13    name_13                                  author_13       12/29/2015 12/29/2015 5   
 14    name_14                                  author_14       12/29/2015 12/29/2015 5   
 15    name_15                                  author_15       12/29/2015 12/29/2015 5   
 16    name_16                                  author_16       12/29/2015 12/29/2015 5   
 17    name_17                                  author_17       12/29/2015 12/29/2015 5   
 18    name_18                                  author_18       12/29/2015 12/29/2015 5   
 19    name_19                                  author_19       12/29/2015 12/29/2015 5   
 2     name_2                                   author_2        12/29/2015 12/29/2015 5   
 20    name_20                                  author_20       12/29/2015 12/29/2015 5   
 21    name_21                                  author_21       12/29/2015 12/29/2015 5   
 22    name_22                                  author_22       12/29/2015 12/29/2015 5   
 23    name_23                                  author_23       12/29/2015 12/29/2015 5   
 24    name_24                                  author_24       12/29/2015 12/29/2015 5   
 25    name_25                                  author_25       12/29/2015 12/29/2015 5   
 26    name_26                                  author_26       12/29/2015 12/29/2015 5   

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
==========================================================================================      Please input your command =========================================================================================
ID     name                                     *author         DoP        DoR        RoS 
_0     name_0                                   author_0        12/29/2015 12/29/2015 5   
 1     name_1                                   author_1        12/29/2015 12/29/2015 5   
 18    name_18                                  author_18       12/29/2015 12/29/2015 5   
 13    name_13                                  author_13       12/29/2015 12/29/2015 5   
 11    name_11                                  author_11       12/29/2015 12/29/2015 5   
 10    name_10                                  author_10       12/29/2015 12/29/2015 5   
 12    name_12                                  author_12       12/29/2015 12/29/2015 5   
 14    name_14                                  author_14       12/29/2015 12/29/2015 5   
 15    name_15                                  author_15       12/29/2015 12/29/2015 5   
 16    name_16                                  author_16       12/29/2015 12/29/2015 5   
 17    name_17                                  author_17       12/29/2015 12/29/2015 5   
 19    name_19                                  author_19       12/29/2015 12/29/2015 5   
 2     name_2                                   author_2        12/29/2015 12/29/2015 5   
 27    name_27                                  author_27       12/29/2015 12/29/2015 5   
 22    name_22                                  author_22       12/29/2015 12/29/2015 5   
 20    name_20                                  author_20       12/29/2015 12/29/2015 5   
 21    name_21                                  author_21       12/29/2015 12/29/2015 5   
 23    name_23                                  author_23       12/29/2015 12/29/2015 5   
 24    name_24                                  author_24       12/29/2015 12/29/2015 5   
 25    name_25                                  author_25       12/29/2015 12/29/2015 5   

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
==========================================================================================      Please input your command =========================================================================================
ID     name                                     author          *DoP       DoR        RoS 
_0     name_0                                   author_0        12/29/2015 12/29/2015 5   
 26    name_26                                  author_26       12/29/2015 12/29/2015 5   
 17    name_17                                  author_17       12/29/2015 12/29/2015 5   
 35    name_35                                  author_35       12/29/2015 12/29/2015 5   
 10    name_10                                  author_10       12/29/2015 12/29/2015 5   
 31    name_31                                  author_31       12/29/2015 12/29/2015 5   
 20    name_20                                  author_20       12/29/2015 12/29/2015 5   
 5     name_5                                   author_5        12/29/2015 12/29/2015 5   
 13    name_13                                  author_13       12/29/2015 12/29/2015 5   
 3     name_3                                   author_3        12/29/2015 12/29/2015 5   
 27    name_27                                  author_27       12/29/2015 12/29/2015 5   
 39    name_39                                  author_39       12/29/2015 12/29/2015 5   
 15    name_15                                  author_15       12/29/2015 12/29/2015 5   
 33    name_33                                  author_33       12/29/2015 12/29/2015 5   
 24    name_24                                  author_24       12/29/2015 12/29/2015 5   
 8     name_8                                   author_8        12/29/2015 12/29/2015 5   
 18    name_18                                  author_18       12/29/2015 12/29/2015 5   
 29    name_29                                  author_29       12/29/2015 12/29/2015 5   
 2     name_2                                   author_2        12/29/2015 12/29/2015 5   
 38    name_38                                  author_38       12/29/2015 12/29/2015 5   

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
==========================================================================================      Please input your command =========================================================================================
*ID    name                                     author          DoP        DoR        RoS 
_0     name_0                                   author_0        12/29/2015 12/29/2015 5   
 1     name_1                                   author_1        12/29/2015 12/29/2015 5   
 2     name_2                                   author_2        12/29/2015 12/29/2015 5   
 3     name_3                                   author_3        12/29/2015 12/29/2015 5   
 4     name_4                                   author_4        12/29/2015 12/29/2015 5   
 5     name_5                                   author_5        12/29/2015 12/29/2015 5   
 6     name_6                                   author_6        12/29/2015 12/29/2015 5   
 7     name_7                                   author_7        12/29/2015 12/29/2015 5   
 8     name_8                                   author_8        12/29/2015 12/29/2015 5   
 9     name_9                                   author_9        12/29/2015 12/29/2015 5   
 10    name_10                                  author_10       12/29/2015 12/29/2015 5   
 11    name_11                                  author_11       12/29/2015 12/29/2015 5   
 12    name_12                                  author_12       12/29/2015 12/29/2015 5   
 13    name_13                                  author_13       12/29/2015 12/29/2015 5   
 14    name_14                                  author_14       12/29/2015 12/29/2015 5   
 15    name_15                                  author_15       12/29/2015 12/29/2015 5   
 16    name_16                                  author_16       12/29/2015 12/29/2015 5   
 17    name_17                                  author_17       12/29/2015 12/29/2015 5   
 18    name_18                                  author_18       12/29/2015 12/29/2015 5   
 19    name_19                                  author_19       12/29/2015 12/29/2015 5   

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
==========================================================================================      Please input your command =========================================================================================
ID     name                                     author          DoP        *DoR       RoS 
_0     name_0                                   author_0        12/29/2015 12/29/2015 5   
 20    name_20                                  author_20       12/29/2015 12/29/2015 5   
 10    name_10                                  author_10       12/29/2015 12/29/2015 5   
 30    name_30                                  author_30       12/29/2015 12/29/2015 5   
 5     name_5                                   author_5        12/29/2015 12/29/2015 5   
 25    name_25                                  author_25       12/29/2015 12/29/2015 5   
 15    name_15                                  author_15       12/29/2015 12/29/2015 5   
 35    name_35                                  author_35       12/29/2015 12/29/2015 5   
 3     name_3                                   author_3        12/29/2015 12/29/2015 5   
 23    name_23                                  author_23       12/29/2015 12/29/2015 5   
 13    name_13                                  author_13       12/29/2015 12/29/2015 5   
 33    name_33                                  author_33       12/29/2015 12/29/2015 5   
 8     name_8                                   author_8        12/29/2015 12/29/2015 5   
 28    name_28                                  author_28       12/29/2015 12/29/2015 5   
 18    name_18                                  author_18       12/29/2015 12/29/2015 5   
 38    name_38                                  author_38       12/29/2015 12/29/2015 5   
 2     name_2                                   author_2        12/29/2015 12/29/2015 5   
 22    name_22                                  author_22       12/29/2015 12/29/2015 5   
 12    name_12                                  author_12       12/29/2015 12/29/2015 5   
 32    name_32                                  author_32       12/29/2015 12/29/2015 5   

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
==========================================================================================      Please input your command =========================================================================================
ID     name                                     author          DoP        DoR        *RoS
_0     name_0                                   author_0        12/29/2015 12/29/2015 5   
 7     name_7                                   author_7        12/29/2015 12/29/2015 5   
 13    name_13                                  author_13       12/29/2015 12/29/2015 5   
 19    name_19                                  author_19       12/29/2015 12/29/2015 5   
 25    name_25                                  author_25       12/29/2015 12/29/2015 5   
 24    name_24                                  author_24       12/29/2015 12/29/2015 5   
 38    name_38                                  author_38       12/29/2015 12/29/2015 5   
 31    name_31                                  author_31       12/29/2015 12/29/2015 5   
 30    name_30                                  author_30       12/29/2015 12/29/2015 5   
 37    name_37                                  author_37       12/29/2015 12/29/2015 5   
 28    name_28                                  author_28       12/29/2015 12/29/2015 5   
 21    name_21                                  author_21       12/29/2015 12/29/2015 5   
 3     name_3                                   author_3        12/29/2015 12/29/2015 5   
 9     name_9                                   author_9        12/29/2015 12/29/2015 5   
 12    name_12                                  author_12       12/29/2015 12/29/2015 5   
 16    name_16                                  author_16       12/29/2015 12/29/2015 5   
 10    name_10                                  author_10       12/29/2015 12/29/2015 5   
 17    name_17                                  author_17       12/29/2015 12/29/2015 5   
 8     name_8                                   author_8        12/29/2015 12/29/2015 5   
 1     name_1                                   author_1        12/29/2015 12/29/2015 5   

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
==========================================================================================      Please input your command Please input book name(type return to skip value): Please input book author(type return to skip value): Please input book DoP(type return to skip value): Please input book DoR(type return to skip value): Please input book RoS(type return to skip value): =========================================================================================
ID     name                                     author          DoP        DoR        *RoS
_0     name_0                                   author_0        12/29/2015 12/29/2015 5   
 7     name_7                                   author_7        12/29/2015 12/29/2015 5   
 13    name_13                                  author_13       12/29/2015 12/29/2015 5   
 19    name_19                                  author_19       12/29/2015 12/29/2015 5   
 25    name_25                                  author_25       12/29/2015 12/29/2015 5   
 24    name_24                                  author_24       12/29/2015 12/29/2015 5   
 38    name_38                                  author_38       12/29/2015 12/29/2015 5   
 31    name_31                                  author_31       12/29/2015 12/29/2015 5   
 30    name_30                                  author_30       12/29/2015 12/29/2015 5   
 37    name_37                                  author_37       12/29/2015 12/29/2015 5   
 28    name_28                                  author_28       12/29/2015 12/29/2015 5   
 21    name_21                                  author_21       12/29/2015 12/29/2015 5   
 3     name_3                                   author_3        12/29/2015 12/29/2015 5   
 9     name_9                                   author_9        12/29/2015 12/29/2015 5   
 12    name_12                                  author_12       12/29/2015 12/29/2015 5   
 16    name_16                                  author_16       12/29/2015 12/29/2015 5   
 10    name_10                                  author_10       12/29/2015 12/29/2015 5   
 17    name_17                                  author_17       12/29/2015 12/29/2015 5   
 8     name_8                                   author_8        12/29/2015 12/29/2015 5   
 1     name_1                                   author_1        12/29/2015 12/29/2015 5   

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
==========================================================================================      Please input your command Please input book name(type return to keep original value): Please input book author(type return to keep original value): Please input book DoP(type return to keep original value): Please input book DoR(type return to keep original value): Please input book RoS(type return to keep original value): =========================================================================================
ID     name                                     author          DoP        DoR        *RoS
_0     name_edit                                author_edit     3/4/2015   3/4/2013   0   
 7     name_7                                   author_7        12/29/2015 12/29/2015 5   
 13    name_13                                  author_13       12/29/2015 12/29/2015 5   
 19    name_19                                  author_19       12/29/2015 12/29/2015 5   
 25    name_25                                  author_25       12/29/2015 12/29/2015 5   
 24    name_24                                  author_24       12/29/2015 12/29/2015 5   
 38    name_38                                  author_38       12/29/2015 12/29/2015 5   
 31    name_31                                  author_31       12/29/2015 12/29/2015 5   
 30    name_30                                  author_30       12/29/2015 12/29/2015 5   
 37    name_37                                  author_37       12/29/2015 12/29/2015 5   
 28    name_28                                  author_28       12/29/2015 12/29/2015 5   
 21    name_21                                  author_21       12/29/2015 12/29/2015 5   
 3     name_3                                   author_3        12/29/2015 12/29/2015 5   
 9     name_9                                   author_9        12/29/2015 12/29/2015 5   
 12    name_12                                  author_12       12/29/2015 12/29/2015 5   
 16    name_16                                  author_16       12/29/2015 12/29/2015 5   
 10    name_10                                  author_10       12/29/2015 12/29/2015 5   
 17    name_17                                  author_17       12/29/2015 12/29/2015 5   
 8     name_8                                   author_8        12/29/2015 12/29/2015 5   
 1     name_1                                   author_1        12/29/2015 12/29/2015 5   

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
==========================================================================================      Please input your command ========================================================================================
ID     : 0
Name   : name_edit
Author : author_edit
DoP    : 3/4/2015
DoR    : 3/4/2013
RoS    : 0

========================================================================================        =========================================================================================
ID     name                                     author          DoP        DoR        *RoS
_0     name_edit                                author_edit     3/4/2015   3/4/2013   0   
 7     name_7                                   author_7        12/29/2015 12/29/2015 5   
 13    name_13                                  author_13       12/29/2015 12/29/2015 5   
 19    name_19                                  author_19       12/29/2015 12/29/2015 5   
 25    name_25                                  author_25       12/29/2015 12/29/2015 5   
 24    name_24                                  author_24       12/29/2015 12/29/2015 5   
 38    name_38                                  author_38       12/29/2015 12/29/2015 5   
 31    name_31                                  author_31       12/29/2015 12/29/2015 5   
 30    name_30                                  author_30       12/29/2015 12/29/2015 5   
 37    name_37                                  author_37       12/29/2015 12/29/2015 5   
 28    name_28                                  author_28       12/29/2015 12/29/2015 5   
 21    name_21                                  author_21       12/29/2015 12/29/2015 5   
 3     name_3                                   author_3        12/29/2015 12/29/2015 5   
 9     name_9                                   author_9        12/29/2015 12/29/2015 5   
 12    name_12                                  author_12       12/29/2015 12/29/2015 5   
 16    name_16                                  author_16       12/29/2015 12/29/2015 5   
 10    name_10                                  author_10       12/29/2015 12/29/2015 5   
 17    name_17                                  author_17       12/29/2015 12/29/2015 5   
 8     name_8                                   author_8        12/29/2015 12/29/2015 5   
 1     name_1                                   author_1        12/29/2015 12/29/2015 5   

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
==========================================================================================      Please input your command Successfully found the following book
========================================================================================
ID     : 35
Name   : name_35
Author : author_35
DoP    : 12/29/2015
DoR    : 12/29/2015
RoS    : 5

========================================================================================        =========================================================================================
ID     name                                     author          DoP        DoR        *RoS
_0     name_edit                                author_edit     3/4/2015   3/4/2013   0   
 7     name_7                                   author_7        12/29/2015 12/29/2015 5   
 13    name_13                                  author_13       12/29/2015 12/29/2015 5   
 19    name_19                                  author_19       12/29/2015 12/29/2015 5   
 25    name_25                                  author_25       12/29/2015 12/29/2015 5   
 24    name_24                                  author_24       12/29/2015 12/29/2015 5   
 38    name_38                                  author_38       12/29/2015 12/29/2015 5   
 31    name_31                                  author_31       12/29/2015 12/29/2015 5   
 30    name_30                                  author_30       12/29/2015 12/29/2015 5   
 37    name_37                                  author_37       12/29/2015 12/29/2015 5   
 28    name_28                                  author_28       12/29/2015 12/29/2015 5   
 21    name_21                                  author_21       12/29/2015 12/29/2015 5   
 3     name_3                                   author_3        12/29/2015 12/29/2015 5   
 9     name_9                                   author_9        12/29/2015 12/29/2015 5   
 12    name_12                                  author_12       12/29/2015 12/29/2015 5   
 16    name_16                                  author_16       12/29/2015 12/29/2015 5   
 10    name_10                                  author_10       12/29/2015 12/29/2015 5   
 17    name_17                                  author_17       12/29/2015 12/29/2015 5   
 8     name_8                                   author_8        12/29/2015 12/29/2015 5   
 1     name_1                                   author_1        12/29/2015 12/29/2015 5   

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
==========================================================================================      Please input your command =========================================================================================
ID     name                                     author          DoP        DoR        *RoS
_7     name_7                                   author_7        12/29/2015 12/29/2015 5   
 13    name_13                                  author_13       12/29/2015 12/29/2015 5   
 19    name_19                                  author_19       12/29/2015 12/29/2015 5   
 25    name_25                                  author_25       12/29/2015 12/29/2015 5   
 24    name_24                                  author_24       12/29/2015 12/29/2015 5   
 38    name_38                                  author_38       12/29/2015 12/29/2015 5   
 31    name_31                                  author_31       12/29/2015 12/29/2015 5   
 30    name_30                                  author_30       12/29/2015 12/29/2015 5   
 37    name_37                                  author_37       12/29/2015 12/29/2015 5   
 28    name_28                                  author_28       12/29/2015 12/29/2015 5   
 21    name_21                                  author_21       12/29/2015 12/29/2015 5   
 3     name_3                                   author_3        12/29/2015 12/29/2015 5   
 9     name_9                                   author_9        12/29/2015 12/29/2015 5   
 12    name_12                                  author_12       12/29/2015 12/29/2015 5   
 16    name_16                                  author_16       12/29/2015 12/29/2015 5   
 10    name_10                                  author_10       12/29/2015 12/29/2015 5   
 17    name_17                                  author_17       12/29/2015 12/29/2015 5   
 8     name_8                                   author_8        12/29/2015 12/29/2015 5   
 1     name_1                                   author_1        12/29/2015 12/29/2015 5   
 35    name_35                                  author_35       12/29/2015 12/29/2015 5   

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
==========================================================================================      Please input your command Please input book name(type return to skip value): =========================================================================================
ID     name                                     author          DoP        DoR        *RoS
_7     name_7                                   author_7        12/29/2015 12/29/2015 5   
 13    name_13                                  author_13       12/29/2015 12/29/2015 5   
 19    name_19                                  author_19       12/29/2015 12/29/2015 5   
 25    name_25                                  author_25       12/29/2015 12/29/2015 5   
 24    name_24                                  author_24       12/29/2015 12/29/2015 5   
 38    name_38                                  author_38       12/29/2015 12/29/2015 5   
 31    name_31                                  author_31       12/29/2015 12/29/2015 5   
 30    name_30                                  author_30       12/29/2015 12/29/2015 5   
 37    name_37                                  author_37       12/29/2015 12/29/2015 5   
 28    name_28                                  author_28       12/29/2015 12/29/2015 5   
 21    name_21                                  author_21       12/29/2015 12/29/2015 5   
 3     name_3                                   author_3        12/29/2015 12/29/2015 5   
 9     name_9                                   author_9        12/29/2015 12/29/2015 5   
 12    name_12                                  author_12       12/29/2015 12/29/2015 5   
 16    name_16                                  author_16       12/29/2015 12/29/2015 5   
 10    name_10                                  author_10       12/29/2015 12/29/2015 5   
 17    name_17                                  author_17       12/29/2015 12/29/2015 5   
 8     name_8                                   author_8        12/29/2015 12/29/2015 5   
 1     name_1                                   author_1        12/29/2015 12/29/2015 5   
 35    name_35                                  author_35       12/29/2015 12/29/2015 5   

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
==========================================================================================      Please input your command =========================================================================================
ID     name                                     author          DoP        DoR        *RoS
_34    name_34                                  author_34       12/29/2015 12/29/2015 5   
 22    name_22                                  author_22       12/29/2015 12/29/2015 5   
 26    name_26                                  author_26       12/29/2015 12/29/2015 5   
 5     name_5                                   author_5        12/29/2015 12/29/2015 5   
 4     name_4                                   author_4        12/29/2015 12/29/2015 5   
 18    name_18                                  author_18       12/29/2015 12/29/2015 5   
 11    name_11                                  author_11       12/29/2015 12/29/2015 5   
 23    name_23                                  author_23       12/29/2015 12/29/2015 5   
 29    name_29                                  author_29       12/29/2015 12/29/2015 5   
 32    name_32                                  author_32       12/29/2015 12/29/2015 5   
 36    name_36                                  author_36       12/29/2015 12/29/2015 5   
 20    name_20                                  author_20       12/29/2015 12/29/2015 5   
 27    name_27                                  author_27       12/29/2015 12/29/2015 5   
 33    name_33                                  author_33       12/29/2015 12/29/2015 5   
 39    name_39                                  author_39       12/29/2015 12/29/2015 5   
 15    name_15                                  author_15       12/29/2015 12/29/2015 5   
 14    name_14                                  author_14       12/29/2015 12/29/2015 5   
 2     name_2                                   author_2        12/29/2015 12/29/2015 5   
 6     name_6                                   author_6        12/29/2015 12/29/2015 5   
 40    name_add                                 author_add      2/3/2014   3/5/2013   5   

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
==========================================================================================      Please input your command =========================================================================================
ID     name                                     author          DoP        DoR        *RoS
_7     name_7                                   author_7        12/29/2015 12/29/2015 5   
 13    name_13                                  author_13       12/29/2015 12/29/2015 5   
 19    name_19                                  author_19       12/29/2015 12/29/2015 5   
 25    name_25                                  author_25       12/29/2015 12/29/2015 5   
 24    name_24                                  author_24       12/29/2015 12/29/2015 5   
 38    name_38                                  author_38       12/29/2015 12/29/2015 5   
 31    name_31                                  author_31       12/29/2015 12/29/2015 5   
 30    name_30                                  author_30       12/29/2015 12/29/2015 5   
 37    name_37                                  author_37       12/29/2015 12/29/2015 5   
 28    name_28                                  author_28       12/29/2015 12/29/2015 5   
 21    name_21                                  author_21       12/29/2015 12/29/2015 5   
 3     name_3                                   author_3        12/29/2015 12/29/2015 5   
 9     name_9                                   author_9        12/29/2015 12/29/2015 5   
 12    name_12                                  author_12       12/29/2015 12/29/2015 5   
 16    name_16                                  author_16       12/29/2015 12/29/2015 5   
 10    name_10                                  author_10       12/29/2015 12/29/2015 5   
 17    name_17                                  author_17       12/29/2015 12/29/2015 5   
 8     name_8                                   author_8        12/29/2015 12/29/2015 5   
 1     name_1                                   author_1        12/29/2015 12/29/2015 5   
 35    name_35                                  author_35       12/29/2015 12/29/2015 5   

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
==========================================================================================      Please input your command =========================================================================================
ID     name                                     author          DoP        DoR        *RoS
 7     name_7                                   author_7        12/29/2015 12/29/2015 5   
_13    name_13                                  author_13       12/29/2015 12/29/2015 5   
 19    name_19                                  author_19       12/29/2015 12/29/2015 5   
 25    name_25                                  author_25       12/29/2015 12/29/2015 5   
 24    name_24                                  author_24       12/29/2015 12/29/2015 5   
 38    name_38                                  author_38       12/29/2015 12/29/2015 5   
 31    name_31                                  author_31       12/29/2015 12/29/2015 5   
 30    name_30                                  author_30       12/29/2015 12/29/2015 5   
 37    name_37                                  author_37       12/29/2015 12/29/2015 5   
 28    name_28                                  author_28       12/29/2015 12/29/2015 5   
 21    name_21                                  author_21       12/29/2015 12/29/2015 5   
 3     name_3                                   author_3        12/29/2015 12/29/2015 5   
 9     name_9                                   author_9        12/29/2015 12/29/2015 5   
 12    name_12                                  author_12       12/29/2015 12/29/2015 5   
 16    name_16                                  author_16       12/29/2015 12/29/2015 5   
 10    name_10                                  author_10       12/29/2015 12/29/2015 5   
 17    name_17                                  author_17       12/29/2015 12/29/2015 5   
 8     name_8                                   author_8        12/29/2015 12/29/2015 5   
 1     name_1                                   author_1        12/29/2015 12/29/2015 5   
 35    name_35                                  author_35       12/29/2015 12/29/2015 5   

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
==========================================================================================      Please input your command =========================================================================================
ID     name                                     author          DoP        DoR        *RoS
_7     name_7                                   author_7        12/29/2015 12/29/2015 5   
 13    name_13                                  author_13       12/29/2015 12/29/2015 5   
 19    name_19                                  author_19       12/29/2015 12/29/2015 5   
 25    name_25                                  author_25       12/29/2015 12/29/2015 5   
 24    name_24                                  author_24       12/29/2015 12/29/2015 5   
 38    name_38                                  author_38       12/29/2015 12/29/2015 5   
 31    name_31                                  author_31       12/29/2015 12/29/2015 5   
 30    name_30                                  author_30       12/29/2015 12/29/2015 5   
 37    name_37                                  author_37       12/29/2015 12/29/2015 5   
 28    name_28                                  author_28       12/29/2015 12/29/2015 5   
 21    name_21                                  author_21       12/29/2015 12/29/2015 5   
 3     name_3                                   author_3        12/29/2015 12/29/2015 5   
 9     name_9                                   author_9        12/29/2015 12/29/2015 5   
 12    name_12                                  author_12       12/29/2015 12/29/2015 5   
 16    name_16                                  author_16       12/29/2015 12/29/2015 5   
 10    name_10                                  author_10       12/29/2015 12/29/2015 5   
 17    name_17                                  author_17       12/29/2015 12/29/2015 5   
 8     name_8                                   author_8        12/29/2015 12/29/2015 5   
 1     name_1                                   author_1        12/29/2015 12/29/2015 5   
 35    name_35                                  author_35       12/29/2015 12/29/2015 5   

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
==========================================================================================      Please input your command \
"""
        res = self.out_file.getvalue()
        refa = ref.split("\n")
        resa = res.split("\n")
        self.assertEqual(len(refa), len(resa))
        for i in xrange(len(resa)):
            self.assertEqual(refa[i], resa[i])

    def testMainViewController(self):
        self.bc.setInputValue("exit")
        self.bc.run()
        self.in_file.truncate(0)
        res = """\
=========================================================================================
*ID    name                                     author          DoP        DoR        RoS 

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
==========================================================================================      Please input your command \
"""
        self.assertEqual(self.bc.out_file.getvalue(), res)

    def testAddViewController(self):
        name = "name1"
        author = "author1"
        dop = "1/3/2016"
        dor = "1/5/2016"
        ros = 1
        add = "%s\n%s\n%s\n%s\n%s" % (name, author, dop, dor, ros)
        command = "add\n" + add + "\n" + "exit"
        self.bc.setInputValue(command)
        self.bc.run()
        res = """\
=========================================================================================
*ID    name                                     author          DoP        DoR        RoS 

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
==========================================================================================      Please input your command Please input book name(type return to skip value): Please input book author(type return to skip value): Please input book DoP(type return to skip value): Please input book DoR(type return to skip value): Please input book RoS(type return to skip value): =========================================================================================
*ID    name                                     author          DoP        DoR        RoS 
_0     name1                                    author1         1/3/2016   1/5/2016   1   

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
==========================================================================================      Please input your command """
        reta = self.out_file.getvalue().split("\n")
        resa = res.split("\n")
        self.assertEqual(len(reta), len(resa))
        for i in xrange(len(reta)):
            self.assertEqual(reta[i], resa[i])

    def testEditViewController(self):
        book = BookModel()
        book.name = "name1"
        book.author = "author1"
        book.DoP = "1/4/2016"
        book.DoR = "3/4/2016"
        book.RoS = 5
        self.bc.bm.add_book(book)
        name = "name2"
        author = "author2"
        DoP = "1/5/2016"
        DoR = "3/5/2016"
        RoS = 4
        add = "%s\n%s\n%s\n%s\n%d\n" % (name, author, DoP, DoR, RoS)
        command = "edit\n" + add + "exit\n"
        self.bc.setInputValue(command)
        self.bc.run()
        ref = """\
=========================================================================================
*ID    name                                     author          DoP        DoR        RoS 
_0     name1                                    author1         1/4/2016   3/4/2016   5   

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
==========================================================================================      Please input your command Please input book name(type return to keep original value): Please input book author(type return to keep original value): Please input book DoP(type return to keep original value): Please input book DoR(type return to keep original value): Please input book RoS(type return to keep original value): =========================================================================================
*ID    name                                     author          DoP        DoR        RoS 
_0     name2                                    author2         1/5/2016   3/5/2016   4   

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
==========================================================================================      Please input your command """
        reta = self.out_file.getvalue().split("\n")
        refa = ref.split("\n")
        self.assertEqual(len(reta), len(refa))
        for i in xrange(len(reta)):
            self.assertEqual(reta[i], refa[i])

    def testViewViewController(self):
        book = BookModel()
        book.name = "name1"
        book.author = "author1"
        book.DoP = "12/29/2015"
        book.DoR = "12/29/2015"
        book.RoS = 5
        self.bc.bm.add_book(book)
        command = "view\nexit\n"
        self.bc.setInputValue(command)
        self.bc.run()
        res = """\
=========================================================================================
*ID    name                                     author          DoP        DoR        RoS 
_0     name1                                    author1         12/29/2015 12/29/2015 5   

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
==========================================================================================      Please input your command ========================================================================================
ID     : 0
Name   : name1
Author : author1
DoP    : 12/29/2015
DoR    : 12/29/2015
RoS    : 5

========================================================================================        =========================================================================================
*ID    name                                     author          DoP        DoR        RoS 
_0     name1                                    author1         12/29/2015 12/29/2015 5   

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
==========================================================================================      Please input your command \
"""
        self.assertEqual(self.out_file.getvalue(), res)

    def testDeleteViewController(self):
        book = BookModel()
        book.name = "name1"
        book.author = "author1"
        book.DoP = "12/29/2015"
        book.DoR = "12/29/2015"
        book.RoS = 5
        self.bc.bm.add_book(book)
        command = "delete\nexit\n"
        self.bc.setInputValue(command)
        self.bc.run()
        ref = """\
=========================================================================================
*ID    name                                     author          DoP        DoR        RoS 
_0     name1                                    author1         12/29/2015 12/29/2015 5   

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
==========================================================================================      Please input your command =========================================================================================
*ID    name                                     author          DoP        DoR        RoS 

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
==========================================================================================      Please input your command """
        self.assertEqual(self.out_file.getvalue(), ref)

    def testPageController(self):
        for i in xrange(21):
            book = BookModel()
            book.name = "name_%d" % i
            book.author = "author_%d" % i
            book.DoP = "12/29/2015"
            book.DoR = "12/29/2015"
            book.RoS = 5
            self.bc.bm.add_book(book)
        command = "n\np\nexit"
        self.bc.setInputValue(command)
        self.bc.run()
        ref = """\
=========================================================================================
*ID    name                                     author          DoP        DoR        RoS 
_0     name_0                                   author_0        12/29/2015 12/29/2015 5   
 1     name_1                                   author_1        12/29/2015 12/29/2015 5   
 2     name_2                                   author_2        12/29/2015 12/29/2015 5   
 3     name_3                                   author_3        12/29/2015 12/29/2015 5   
 4     name_4                                   author_4        12/29/2015 12/29/2015 5   
 5     name_5                                   author_5        12/29/2015 12/29/2015 5   
 6     name_6                                   author_6        12/29/2015 12/29/2015 5   
 7     name_7                                   author_7        12/29/2015 12/29/2015 5   
 8     name_8                                   author_8        12/29/2015 12/29/2015 5   
 9     name_9                                   author_9        12/29/2015 12/29/2015 5   
 10    name_10                                  author_10       12/29/2015 12/29/2015 5   
 11    name_11                                  author_11       12/29/2015 12/29/2015 5   
 12    name_12                                  author_12       12/29/2015 12/29/2015 5   
 13    name_13                                  author_13       12/29/2015 12/29/2015 5   
 14    name_14                                  author_14       12/29/2015 12/29/2015 5   
 15    name_15                                  author_15       12/29/2015 12/29/2015 5   
 16    name_16                                  author_16       12/29/2015 12/29/2015 5   
 17    name_17                                  author_17       12/29/2015 12/29/2015 5   
 18    name_18                                  author_18       12/29/2015 12/29/2015 5   
 19    name_19                                  author_19       12/29/2015 12/29/2015 5   

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
==========================================================================================      Please input your command =========================================================================================
*ID    name                                     author          DoP        DoR        RoS 
_20    name_20                                  author_20       12/29/2015 12/29/2015 5   

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
==========================================================================================      Please input your command =========================================================================================
*ID    name                                     author          DoP        DoR        RoS 
_0     name_0                                   author_0        12/29/2015 12/29/2015 5   
 1     name_1                                   author_1        12/29/2015 12/29/2015 5   
 2     name_2                                   author_2        12/29/2015 12/29/2015 5   
 3     name_3                                   author_3        12/29/2015 12/29/2015 5   
 4     name_4                                   author_4        12/29/2015 12/29/2015 5   
 5     name_5                                   author_5        12/29/2015 12/29/2015 5   
 6     name_6                                   author_6        12/29/2015 12/29/2015 5   
 7     name_7                                   author_7        12/29/2015 12/29/2015 5   
 8     name_8                                   author_8        12/29/2015 12/29/2015 5   
 9     name_9                                   author_9        12/29/2015 12/29/2015 5   
 10    name_10                                  author_10       12/29/2015 12/29/2015 5   
 11    name_11                                  author_11       12/29/2015 12/29/2015 5   
 12    name_12                                  author_12       12/29/2015 12/29/2015 5   
 13    name_13                                  author_13       12/29/2015 12/29/2015 5   
 14    name_14                                  author_14       12/29/2015 12/29/2015 5   
 15    name_15                                  author_15       12/29/2015 12/29/2015 5   
 16    name_16                                  author_16       12/29/2015 12/29/2015 5   
 17    name_17                                  author_17       12/29/2015 12/29/2015 5   
 18    name_18                                  author_18       12/29/2015 12/29/2015 5   
 19    name_19                                  author_19       12/29/2015 12/29/2015 5   

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
==========================================================================================      Please input your command \
"""
        self.assertEqual(self.out_file.getvalue(), ref)

