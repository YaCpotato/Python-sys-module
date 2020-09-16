"""
$ python check_argv.py 1 apple [1,2,3]
check_argv.py
<class 'str'>
1
<class 'str'>
apple
<class 'str'>
[1,2,3]
<class 'str'>
"""

import sys

if __name__ == '__main__':

	for w in sys.argv:
		print(w)
		print(type(w))
