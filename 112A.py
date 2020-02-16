string1 = input().lower()
string2 = input().lower()
if len(string1)>len(string2):
	n = len(string1)
elif len(string1)<len(string2):
	n = len(string2)
elif len(string1)==len(string2):
	n = len(string2)
for i in range(n):
	if string2[i]>string1[i]:
		print("-1")
		break
	elif string2[i]<string1[i]:
		print("1")
		break
	elif i == n-1 and string2[i]==string1[i]:
		print(0)
