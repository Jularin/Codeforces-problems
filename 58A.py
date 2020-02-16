string = input()
List = ["h","e","l","l","o",]
counter = 0
for letter in List:
	if string.find(letter)!=-1:
		string = string[string.find(letter)+1:]
		counter += 1
	else:
		counter-=1
if counter==5:
	print("YES")
else:
	print("NO")