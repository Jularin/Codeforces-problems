k2,k3,k5,k6 = map(int, input().split())
summa = 0

for i in range(5000001):
    if k2>0 and k5>0 and k6>0:
        summa+=256
        k2-=1
        k5-=1
        k6-=1
    else:
        break
for i in range(50000001):
    if k2>0 and k3>0:
        summa+=32
        k2-=1
        k3-=1
    else:
        break
print(summa)
