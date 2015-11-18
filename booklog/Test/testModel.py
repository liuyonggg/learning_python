
import unittest

from Model.Model import *

class TestModel(unittest.TestCase):
    def test_model(self):
        t = Model()
        assert (t)
        t.serialize()
        t.deserialize('')
    
    def test_book_model_property(self):
        t = BookModel()
        t.ID = 0
        self.assertEqual(t.ID, 0)
        self.assertEqual(t._ID, 0)
        t.name  = "test"
        self.assertEqual(t.name, 'test')
        t.author = "bob"
        self.assertEqual(t.author, 'bob')
        t.DoP = datetime.date(2015, 11, 16)
        self.assertEqual(t.DoP, datetime.date(2015, 11, 16))
        t.DoR = datetime.date(2014, 11, 16)
        self.assertEqual(t.DoR, datetime.date(2014, 11, 16))
        t.RoS = 0
        self.assertEqual(t.RoS, 0)


    def test_book_model_compare(self):
        t1 = BookModel()
        t1.ID = 0
        t1.name  = "test"
        t1.author = "bob"
        t1.DoP = datetime.date(2015, 11, 16)
        t1.DoR = datetime.date(2014, 11, 16)
        t1.RoS = 0

        t2 = BookModel()
        t2.ID = 1
        t2.name  = "tset"
        t2.author = "joe"
        t2.DoP = datetime.date(2016, 11, 16)
        t2.DoR = datetime.date(2015, 11, 16)
        t2.RoS = 1

        self.assertEqual(t1.compare_by_ID(t2), -1)
        self.assertEqual(t2.compare_by_ID(t1), 1)
        self.assertEqual(t1.compare_by_ID(t1), 0)
        self.assertEqual(t2.compare_by_ID(t2), 0)


        self.assertEqual(t1.compare_by_name(t2), -1)
        self.assertEqual(t2.compare_by_name(t1), 1)
        self.assertEqual(t1.compare_by_name(t1), 0)
        self.assertEqual(t2.compare_by_name(t2), 0)

        self.assertEqual(t1.compare_by_author(t2), -1)
        self.assertEqual(t2.compare_by_author(t1), 1)
        self.assertEqual(t1.compare_by_author(t1), 0)
        self.assertEqual(t2.compare_by_author(t2), 0)

        self.assertEqual(t1.compare_by_DoP(t2), -1)
        self.assertEqual(t2.compare_by_DoP(t1), 1)
        self.assertEqual(t1.compare_by_DoP(t1), 0)
        self.assertEqual(t2.compare_by_DoP(t2), 0)


        self.assertEqual(t1.compare_by_DoR(t2), -1)
        self.assertEqual(t2.compare_by_DoR(t1), 1)
        self.assertEqual(t1.compare_by_DoR(t1), 0)
        self.assertEqual(t2.compare_by_DoR(t2), 0)

        self.assertEqual(t1.compare_by_RoS(t2), -1)
        self.assertEqual(t2.compare_by_RoS(t1), 1)
        self.assertEqual(t1.compare_by_RoS(t1), 0)
        self.assertEqual(t2.compare_by_RoS(t2), 0)


    def test_book_model_compare(self):
        t1 = BookModel()
        t1.ID = 0
        t1.name  = "test"
        t1.author = "bob"
        t1.DoP = datetime.date(2015, 11, 16)
        t1.DoR = datetime.date(2014, 11, 16)
        t1.RoS = 0

        s = t1.serialize()
        self.assertEqual(s, "0\ntest\nbob\n2015-11-16\n2014-11-16\n0\n")
        t2 = BookModel()
        t2.deserialize(s)
        self.assertEqual(t1, t2)

if __name__ == '__main__':
    unittest.main()
