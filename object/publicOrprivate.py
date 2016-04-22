__author__ = 'muli'

class Person():
    pupulation = 0
    __address__ = "1"

    def __init__(self, name):
        self.name = name
        Person.pupulation += 1
        print("add name", name)

    def __del__(self):
        Person.pupulation -= 1
        print("del name", self.name)

    def sayhi(self):
        print("hi", self.name)

    def howMany(self):
        print("all:", Person.pupulation)


a = Person("zhangsan")
a.__address__ = "aaa"
b = Person("lisi")
# b.__address__ = "bbb"

print(a.__address__)
print(b.__address__)

# print(a.pupulation)
# print(b.pupulation)

# print(a.sayhi())

del a
del b