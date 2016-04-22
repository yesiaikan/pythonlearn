import sys

__author__ = 'muli'

a = ['1', '2', '3', '4']
assert (4 == len(a))
print("---")
print(sys.argv)

assert "1"==a[0]
assert 'carrot'.startswith('car')
assert 'ro' in 'carrot'              #判断字符串是否包含