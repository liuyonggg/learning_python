import unittest
from Model.Model import *
from View.View import *
from Controller.Controller import *
import StringIO

class ControllerTest(unittest.TestCase):
    def setUp(self):
        self.in_file = self.out_file = StringIO.StringIO()
        self.db_file = []
        
    def testMainViewController(self):
        bc = BookController(self.in_file, self.out_file, self.db_file)
        bc.run()
        bc.command_handler("exit")
        #self.assertEqual(out_file.getValue(), "")
