numbers = [0,1,2,3,4,5,6,7,8,9]
steps = 0
n = 5
closed = 82195
opened = 64723
for i in range(n):
	number_closed = closed%10
	number_opened = opened%10
	if number_opened == number_closed:
		steps+=0
	elif number_closed < number_opened:
		number_closed1=number_closed +10
		if abs(number_opened -number_closed)<number_closed1 - number_opened:
			steps+= abs(number_opened - number_closed)
		elif abs(number_opened -number_closed)>number_closed1 - number_opened:
			steps+= number_closed1 - number_opened

	elif number_closed > number_opened:
		number_opened1 =number_opened + 10
		if abs(number_opened -number_closed)<number_opened1 - number_opened:
			steps+=abs(number_opened - number_closed)
		elif abs(number_opened -number_closed)>number_opened1 - number_opened:
			steps+=number_opened1 - number_opened

print(steps)
"""NOT SOLVED"""
