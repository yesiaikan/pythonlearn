import unittest
from first import First

__author__ = 'muli'


def suite():
    suite = unittest.TestSuite()
    suite.addTest(First("test1"))
    suite.addTest(First("test3"))
    return suite

