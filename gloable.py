__author__ = 'muli'
__name__ = "gloable name"

#全局变量
def myglobal():
    global a
    print(a, "two")
    a = 100
    print(a, "three")

a = 1
print(a, "one")
myglobal()
print(a, "foure")

print("----------------------- 1")

#局部变量
def func(x):
    print("x is", x)
    x = 100
    print("x is", x)

x = 10
print("x is", x)
func(x)
print("x is", x)

print("----------------------- 2")

#默认参数
def say(x, y=5):
    print(x*y)
x = 5
say(x)
say(x, 2)
say("abcde")
say("12345")
print("5次" * 5)

print("----------------------- 3")

#返回值参数
def maxnum(x, y):
    if x > y:
        return x
    else:
        return y

print (maxnum(1, 5))

print("----------------------- 4")

#文档字符串
def maxnum(x, y):
    """Pint:

    kldsaflksdjfl"""
    if x > y:
        return x
    else:
        return y

print (maxnum(1, 5))
print (maxnum.__doc__)  #文档内容
print(__file__)         #文件路径

print("---------------------- 5")
#dir()
print(dir())
print(__loader__)

