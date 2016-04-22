import json
from myjson.Student import Student

__author__ = 'muli'

student = Student('zhangsan', 11)

j = json.load(student)

