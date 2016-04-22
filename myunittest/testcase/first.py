import unittest
import xmlrunner

__author__ = 'muli'
#encoding:utf-8

class First(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print 'setup class\n'

    @classmethod
    def tearDownClass(cls):
        print 'teardown class\n'

    def setUp(self):
        print 'setup'

    def tearDown(self):
        print 'teardown\n'

    @unittest.skip('no reason skip test1')
    def test1(self):
        print '11111111111'

    def test2(self):
        print '22222222222'

    @unittest.skipIf(1 < 3, '1 compare with 3')
    def test4(self):
        print '44444444444'

    def test3(self):
        print '33333333333'

    def test5(self):
        self.assertEqual(2, 2)

    def test6(self):
        print dir(unittest)
        print '6666666'


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(First)
    xmlrunner.XMLTestRunner().run(suite)
