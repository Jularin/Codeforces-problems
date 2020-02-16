string = input()
List = []
string1 = ""
for i in string:
	if i!="+":
		List.append(i)
List = sorted(List)

for i in List:
	if string1 == "":
		string1 = i
	else:
		string1= string1+"+"+i
print(string1)