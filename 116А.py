n = int(input())
passangers = 0
max_passangers = []
for i in range(n):
	out,inp = map(int, input().split())
	passangers+= inp-out
	max_passangers.append(passangers)
print(max(max_passangers))