string = input()
up = 0
low = 0
for i in string:
    if i.isupper():
        up+=1
    elif i.islower():
        low+=1
if low>=up:
    print(string.lower())
else:
    print(string.upper())
