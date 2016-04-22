import thread
import time

__author__ = 'muli'


def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print '%s: %s' % (threadName, time.ctime(time.time()))

try:
    thread.start_new_thread(print_time, ("c", 1))
    # thread.start_new_thread(print_time, ("a", 1))
    thread.start_new_thread(print_time('b', 2))
except:
    print 'error'

while 1:
    pass