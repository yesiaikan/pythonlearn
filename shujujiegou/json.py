__author__ = 'muli'
#coding=utf-8

ab = {       'Swaroop'   : 'swaroopch@byteofpython.info',
             'Larry'     : 'larry@wall.org',
             'Matsumoto' : 'matz@ruby-lang.org',
             'Spammer'   : 'spammer@hotmail.com'
     }

print ("Swaroop's address is %s" % ab['Swaroop'])

# Adding a key/value pair
ab['Guido'] = 'guido@python.org'                                    #添加

# Deleting a key/value pair
del ab['Spammer']                                                   #删除

print ('\nThere are %d contacts in the address-book\n' % len(ab))
for name, address in ab.items():                                    #遍历
    print ('Contact %s at %s' % (name, address))

if 'Guido' in ab: # OR ab.has_key('Guido')                          #判断是否存在
    print ("\nGuido's address is %s" % ab['Guido'])


for a, b in ab.items():
    print('key: %s\tvalue:%s' % (a, b))


print("---------------------------------- 序列")

shop = ['a', 'b', 'c', 'dd', 'ee']

print(shop[1])
print(shop[-1])
print(shop[1:3])
print(shop[2:])
print(shop[1: -1])



name = "zhangsan"
print(name)
print(name[1])
print(name[-1])
print(name[1:-1])
print(name[:3])
print(name[3:])
print(name[:])

print("---------- more about string ------------")
name = "Zhaoliu"
if name.startswith("zhao"):
    print("zhao")
elif name.startswith("Zhao"):
    print("Zhao")
else:
    print("Zhaoliu")

if name.find("zhao"):
    print("zhao 家人")

if name.find("haha") == -1:
    print("no haha")
elif name.find("heihei") == -1:
    print("no heihei")

delimiter='_*_'
innter = "&"
a = ['12', '33', '44']
print(delimiter.join(a))
print(innter.join(a))               #连接列表

print(name.find("Zhao")) #0
print(name.find("zhao")) #-1

