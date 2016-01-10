import unittest
import StringIO
import __builtin__
import sys
import tempfile
import os

class MyIO(object):
    def __init__(self):
        self.value = None

    def getValue(self):
        self.value = raw_input("please input value: ")
        return self.value

    def displayValue(self):
        print (self.value)


class TestIO(unittest.TestCase):
    def setUp(self):
        pass

    def testStringIO(self):
        __builtin__.raw_input = lambda _: 'yes'
        io = MyIO()
        ret = io.getValue()
        self.assertEqual(ret, "yes")
        o = StringIO.StringIO()
        sys.stdout = o
        io.displayValue()
        self.assertEqual(o.getvalue(), "yes\n")
        sys.stdout = sys.__stdout__

    def testFile(self):
        f = tempfile.NamedTemporaryFile(delete=False)
        name = f.name
        f.write("hello\n")
        f.write("world")
        f.close()

        f2 = open(name, "r+")
        s = "".join(f2.readlines())
        self.assertEqual(s, "hello\nworld")
        f2.truncate(0)
        f2.seek(0)
        f2.write("california")
        f2.close()

        f3 = open(name, "r+")
        s = "".join(f3.readlines())
        self.assertEqual(s, "california")
        f3.close()

        os.unlink(name)
        self.assertFalse(os.path.exists(f.name))
