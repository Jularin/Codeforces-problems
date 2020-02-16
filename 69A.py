n = int(input())
List = []
Liist = []
for i in range(n):
	List.append(input().split())
for i in List:
	llist = []
	for x in i:
		llist.append(int(x))
	Liist.append(llist)
marker = "YES"
lir = []
for i in range(3):
	value = 0
	for x in range(n):
		LList =Liist[x]
		value += LList[i]
	if value != 0:
		marker = "NO"
print(marker)