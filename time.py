import calendar
import time

__author__ = 'muli'

print "-------------------"

print "has passed ms", time.time()

print "local current time:", time.localtime(time.time())

print "asc time:", time.asctime(time.localtime(time.time()))

print "-------------------"



print "calendar:", calendar.month(2020, 6)