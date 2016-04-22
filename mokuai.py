__author__ = 'muli'

import sys
import gloable

print ('The command line arguments are:')
for i in sys.argv:
    print (i)
    print("----")

print ('The PYTHONPATH is', sys.path, '')

print("------------------------ 1 ")

if __name__ ==  '__main__':
    print("self")
else:
    print("other")


print("------------------------ 2 ")

if gloable.__name__ == 'gloable name':
    print("other")
else:
    print("self")