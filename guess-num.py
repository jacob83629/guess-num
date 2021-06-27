import random
r = random.randint(1, 100)
count = 0
while True:
	num = input('請猜數字:')
	num = int(num)
	count += 1
	print('你猜了', count, '次了喔!!')
	if r == num:
		print('恭喜答對了')
		break
	elif r > num:
		print('數字再大:')
	else:
		print('數字再小')
