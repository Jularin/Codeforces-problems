n,k = input().split()
n = int(n)
k = int(k)
List = input().split()
for x in range(len(List)):
	List[x] = int(List[x])
summ = 0
try:
        for i in List:
                if i>0:
                        if i>=List[k-1]:
                                summ+=1
except Expection:
        pass
print(summ)
