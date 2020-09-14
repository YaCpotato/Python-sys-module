import sys, os

number = 2

print('1', end=' ')

try:
	print('2\n')
	sys.exit()
except SystemExit as se:
	print('3')
	print('4')

try:
	print('5\n')

	if number == 2:
		exit()
	print('6')
except:
	print('7')
else:
	print('8')

finally:
	print('9')

try:
	number = 4

	if number > 3:
		os._exit(400)
		print('10')
finally:
	print('11')



