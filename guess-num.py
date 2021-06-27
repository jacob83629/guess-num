import random
start = input('請決定數字開始值: ')
end = input('請決定數字結束值: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
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
