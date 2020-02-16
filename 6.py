n = int(input())
List = []
for i in range(n):
	List.append(input().split())
summ = 0
Lisst = []
for i in List:
	llist = []
	for x in i:
		llist.append(int(x))
	Lisst.append(llist)
for a in Lisst:
	if sum(a)>=2:
		summ+=1
print(summ)