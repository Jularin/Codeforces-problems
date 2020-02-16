n = int(input())
List = input().split()
for i in range(n):
    List[i]= int(List[i])
count = 0
List_with_counts = []
try:
    for i in range(n):
        if List[i]<=List[i+1]:
            count+=1
        elif List[i]>List[i+1]:
            List_with_counts.append(count)
            count = 0
except Exception:
    pass
print(max(List_with_counts))
print(List_with_counts)
