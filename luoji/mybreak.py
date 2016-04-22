from pip.backwardcompat import raw_input

__author__ = 'muli'
while True:
    s = raw_input("Enter somthing :")
    if s == "abc":
        break
    print("length of the string is", len(s))
print("Done")