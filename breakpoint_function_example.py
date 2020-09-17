import sys,random,time

def my_debug_function():
	print('.' ,end = '')
	time.sleep(1)
	print('.' ,end = '')
	time.sleep(1)
	print('.')
	time.sleep(2)
	print('俺は止まんねぇからよ、お前らが止まんねぇかぎり、その先に俺はいるぞ！')
	time.sleep(3)
	print('だからよ、、、、')
	time.sleep(4)
	print('止まるんじゃねえぞ、、、。')
	return

sys.breakpointhook = my_debug_function

if __name__ == '__main__':
	breakpoint()
