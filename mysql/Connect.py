import MySQLdb
#encoding:utf-8

__author__ = 'muli'

print 'begain'

db = MySQLdb.connect('10.202.26.41', 'appdigger', 'qad', 'appdigger_test', 8100)

cursor = db.cursor()

cursor.execute('SELECT VERSION()')

data = cursor.fetchone()

print data

db.close()