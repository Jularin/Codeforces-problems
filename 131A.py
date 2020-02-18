string = input()
if string.isupper():
    print(string.swapcase())
elif string[1:].isupper():
    print(string.swapcase())
elif len(string)==1 and string[0].islower():
    print(string.swapcase())
else:
    print(string)
