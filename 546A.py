k,n,w = map(int, input().split())
summ = ((2*k+k*(w-1))*w)/2
if summ<=n:
	print(0)
else:
	print(int(summ-n))