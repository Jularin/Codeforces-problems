summ = 0
n = int(input())
List = []
for i in range(n):
	List.append(input())
for x in List:
	if x =="X++" or x=="++X":
		summ += 1
	elif x == "X--" or x =="--X":
		summ -= 1
print(summ)