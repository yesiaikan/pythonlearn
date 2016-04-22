import os

# __author__ = 'muli'
parm = """abcdalsjfl
lsdajf;lj
lasdjfl;aj

jfjasdlfj"""
#
# f = open('parm.txt', 'w')
# f.write(parm)
# f.close()
# print f.mode
#
# f = open('parm.txt')
# while True:
#     line = f.readline()
#     if len(line) == 0:
#         break
#     print(line)
# f.close()
#
# print '------------------- read()'
# f = open('parm.txt', 'r')
# str = f.read()
# print str
# f.close()
#
# print '------------------- read(8)'
# f = open('parm.txt', 'r')
# s = f.read(8)
# print s
# f.close()
#
# print '------------------- rename()'
# print '------------------- remove()'
# os.rename('parm.txt', 'test.txt');
# os.remove('test.txt')
#
# # os.mkdir("test")
# os.rmdir("newdir")
# os.chdir("test")
# ff= open('parm.txt', 'w')
# ff.write(parm)
#

# fw = open('parm.txt', 'w')
# fw.write(parm)
# fw.close()


# fp = open('parm.txt', 'r')
# lines = fp.readlines()
# for line in lines:
#     print line
# fp.close()

# with open('parm.txt', 'r') as handle:
#     for line in filter(None, handle):
#         print(line)

# for line in open('parm.txt', 'r'):
#     print(line)

with open('parm.txt', 'r') as handle:
    for line in handle:
        print(line)

print(1)
print(2)
print(3)
