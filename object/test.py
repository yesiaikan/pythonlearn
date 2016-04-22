__author__ = 'muli'

class Person():
    pass
p = Person()
print(p)


print("--------------------------")
class say():
    def sayhi(self):
        print("hi world")
s = say()
s.sayhi()


print("--------------------------")
class do():
    def __init__(self, n):
        self.name = n;
    def dosothing(self):
        print("my name is", self.name)
d = do("zhangsan")
d.dosothing()
print(d.name)
print("--------------------------")



a={"muli":'\muli'}
