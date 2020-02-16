n,k = map(int, input().split())
List1 = []
List2 = []
for i in range(1,n+1):
	if i%2==0:
		List1.append(i)
	else:
		List2.append(i)
List1 = List2+List1
print(List1[k-1])