import os
import sys
import re
import unittest
import xmlrunner

__author__ = 'muli'
#encoding:utf-8

class module(unittest.TestCase):

    def setUp(self):
        pass

def testAll():

    path = os.path.abspath(os.path.dirname(sys.argv[0]))

    files = os.listdir(path)

    # test = re.compile("test\.py{1}quot;, re.IGNORECASE()")
    #
    # files = filter(test.search, files)

    files = ['testFirst.py']

    finameToModuleName = lambda f : os.path.splitext(f)[0]

    moduleName = map(finameToModuleName, files)

    module = map(__import__, moduleName)

    load = unittest.TestLoader.loadTestsFromModule

    return unittest.TestSuite(map(load, module))

unittest.TextTestRunner.run(testAll())
#
# suit = unittest.defaultTestLoader.loadTestsFromModule("testAll")
# xmlrunner.XMLTestRunner().run(suit)
