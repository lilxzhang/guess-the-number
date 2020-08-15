import random 
while True:
	r = random. randint(1, 5)
	x = input('guess the number: ')
	x = int(x)
	if x == r:
		print('you guess the right number')
		break
	if x < r:
		print('smaller then answer')
	elif x > r:
		print('greater then aswer')