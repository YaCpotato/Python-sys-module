import sys,time

if __name__ == '__main__':
	start = time.time()
	input_func = input()
	total = time.time() - start
	print(input_func)

	print(r"input() function's ETS is ",float(total))

	start = time.time()
	stdin_func = sys.stdin.readline()
	total = time.time() - start
	print(stdin_func)
	print(r"sys.stdin.readline() function's ETS is ",float(total))
