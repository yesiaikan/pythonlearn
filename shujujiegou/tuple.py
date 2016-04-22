__author__ = 'muli'

yuanZu = ()
print("size:", len(yuanZu))

b = ("a", )
print("size:", len(b))

c = ("b")
print("size:", len(c))

d = ("d", "e")
print("size:", len(d))
print("all:", d)

e = ("1", "2")
print("size:", len(e))
print("all:", e)

f = ('1d23', '2', ('3', '4'))
print("size:", len(f))
print("all:", f)
print("3:", f[2])

g = (1, 2, 3, 4)
print("size:", len(g))
print("all:", g)


print("---------------------------")

age = 18
name = "zhangsan"
print('%s is %d years old' % (name, age))

print("his age is %d" % age)
