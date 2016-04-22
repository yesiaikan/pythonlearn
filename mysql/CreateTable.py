import MySQLdb

__author__ = 'muli'

print 'begain'

db = MySQLdb.connect('10.202.26.41', 'appdigger', 'qad', 'appdigger_test', 8100)

cursor = db.cursor()

sql_dorp = '''drop table if exists students'''

cursor.execute(sql_dorp)

sql = '''create table students(
        name char(20) not null,
        address char(20),
        age int
        )'''

cursor.execute(sql)


db.close()
