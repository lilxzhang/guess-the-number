import random 
y = input('please enter your starting number: ')
e = input('please enter your ending number: ')
y = int(y)
e = int(e)
r = random. randint(y, e)
z = 0
while True:
	z += 1 
	x = input('guess the number: ')
	x = int(x)
	if x == r:
		print('you guess the right number')
		break
	elif x < r:
		print('smaller then answer')
	elif x > r:
		print('greater then aswer')
	print('this is your' , z, 'times guesing')