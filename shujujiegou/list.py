__author__ = 'muli'
#coding=utf-8


shoplist = ['apple', 'mango', 'carrot', 'banana']

print ('I have', len(shoplist),'items to purchase.')

for item in shoplist:                                  #遍历
    print (item),

print ('\nI also have to buy rice.')
shoplist.append('rice')                                 #添加
print ('My shopping list is now', shoplist)

print ('I will sort my list now')
shoplist.sort()                                         #排序
print ('Sorted shopping list is', shoplist)

print ('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]                                        #删除
print ('I bought the', olditem)
print ('My shopping list is now', shoplist )

shoplist[0] = "test"
print ('My shopping list is now', shoplist )

for nem in shoplist:
    print(nem)

b = '-'.join(shoplist)
print b


l = [1, 3, 4, 5,6,7]
def mysort(l):
    for i in range(len(l)):
        for j in range(i, len(l), 1):
            if l[i] > l[j]:
                tmp = l[i]
                l[i] = l[j]
                l[j] = tmp
    print(l)

mysort(l)
print(len(l))

