import os

__author__ = 'muli'

# print(os.listdir('.'))
# print(os.getcwd())
# print(os.listdir(os.getcwd()))
# print(os.mkdir('new'))
# print(os.rmdir('new'))
# print(os.makedirs('new/a/b/c'))
# os.removedirs('new/a/b/c')
# os.walk(os.getcwd())
path = '/home/muli/local/test/untitled'
res = []
def getpy(path):
    for root, directory, files in os.walk(path):
        for filename in files:
            name, suf = os.path.splitext(filename)
            if suf == '.py':
                res.append(os.path.join(root, filename))
        for dir in directory:
            getpy(dir)

getpy(path)
print(res)


l = [1, 6, 4, 2, 76, 34]
def sort(l):
    for i in range(0, len(l), 1):
        for j in range(i, len(l), 1):
            if l[i] > l[j]:
                tmp = l[j]
                l[j] = l[i]
                l[i] = tmp
    print(l)

sort(l)

