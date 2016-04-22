__author__ = 'muli'

def quickSort(l, L, R):
    i = L
    j = R
    v = l[(i + j) / 2]
    while(i<=j):
        while(l[i] < v):
            i+=1
        while(l[j] > v):
            j-=1
        if(i<=j):
            tmp = l[i]
            l[i] = l[j]
            l[j] = tmp
            i+=1
            j-=1
    if(L < j):
        quickSort(l, L, j)
    if(R > i):
        quickSort(l, i, R)

list = [7, 4, 23, 2, 45, 23, 64, 234, 233, 213]
# print(len(list))
# print(range(len(list)))
# quickSort(list, 0, len(list)-1)
# print(list)

def delsame(list):
    list.sort()
    for i in range(len(list)):
        if i == len(list)-1:
            break
        if list[i] == list[i+1]:
            del list[i]

delsame(list)
print(list)