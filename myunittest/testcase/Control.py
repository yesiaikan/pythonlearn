import unittest
import xmlrunner
import test
import first
__author__ = 'muli'

class Control(unittest.TestCase):

    def testSuit(self):
        suite = unittest.TestSuite()
        suite.addTest(test)
        suite.addTest(first)


suite = unittest.TestLoader().loadTestsFromTestCase(Control)
xmlrunner.XMLTestRunner().run(suite)


