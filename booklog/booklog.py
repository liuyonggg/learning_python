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
from Controller.Controller import *
import StringIO
import sys

class InWrapper(object):
    def __init__(self, io):
        self.io = io

    def getvalue(self):
        return self.io.readline()

if __name__ == "__main__":
    #out_file = StringIO.StringIO()
    #in_file = StringIO.StringIO()
    in_file = InWrapper(sys.stdin)
    out_file = sys.stdout
    try:
        db_file = open('datebase.txt', 'r+')
    except IOError:
        db_file = open('datebase.txt', 'w+')
    bc = BookController(in_file,out_file, db_file)
    bc.run()
    db_file.close()
