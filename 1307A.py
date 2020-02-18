t = int(input())
for i in range(t):
    n,day = map(int, input().split())
    haystecks = list(map(int,input().split()))
    iter = 1
    while day>0:
        if n>1:
            try:
                if haystecks[iter]>0:
                    haystecks[iter-1]+=1
                    haystecks[iter]-=1
                    day -=1
                    iter = 1
                else:
                    iter+=1
            except:
                break
        else:
            break
    print(haystecks[0])
