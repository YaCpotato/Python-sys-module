import sys, os

if __name__ == '__main__':

	number = 200

	print('Hello', end=' ')

	try:
		print('World is not exit!\n')
		sys.exit()
	except SystemExit as se:
		print('except SystemExit catched sys.exit()')
		print('this is no error code with exit()')
		print(se.args)

	try:
		print('World is not exit!\n')

		if number == 200:
			sys.exit()
		print('Oh')
	except:
		print('Hey! I like Python')

	finally:
		print('this is finally')

	try:
		number = 400

		if number > 300:
			os._exit(400)
	finally:
		print('This is end?')



