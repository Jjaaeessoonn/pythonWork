import sys
import os
import signal  #h handles ctrl+c/SIGINT

'''
Practice for Python
'''

# Functions

def keyboardInterruptHandler(signalNum, frame):
	#print('KeyboardInterrupt/SIGINT: {0} is caught...'.format(signal) )
	print('In error handler')
	sys.exit(0)

signal.signal(signal.SIGINT, keyboardInterruptHandler)

def genInfiniteIncrement():
	'''
	Generator of infinite increments by 1
	'''
	x = 1

	while (True):
		yield x
		x += 1

def files():
	with open(filePath, 'r') as f:
		contents = f.readlines()

		with open(filePath + 'Written', 'w') as w:
			w.writelines(contents)

def echo():
	try:
		while (True):
			entry = input('Enter something: ')
			print(entry)
	except:
		print('Exception!')

	return

def extend(func):
	def dec(x):
		print('calling a directory')
		func(x)
	return dec

@extend
def dirTree(cmd):
	dirCmd = {
		'file': files,
		'echo': echo

	}

	return dirCmd.get(cmd, 'Invalid cmd')

# Classes

class Person:
	def __init__(self, name, age, *details):
		self.name = name
		self.age = age
		self.misc = details

	def func(self):
		print(self.name + '\'s func')



if __name__ == '__main__':

	if len(sys.argv) > 1:
		filePath = sys.argv[1]

	contents = []     #list that has numbered indices, can contain objects of different types
	diction = {}      #list with generalized, immutable indices
	tup = 1, 2, 3     #same as (1, 2, 3)
	text = 'xyz'      #basically a tuple of chars

	lstCubed = [i**3 for i in range(5)]  #list comprehension
	map(lambda x:x**2, lstCubed)
	filter(lambda x:x%2 == 0, lstCubed)


	try:

		while(True):
			cmd = input('Enter command: ')
			
			if len(sys.argv) > 1 and cmd == 'file':
				print('No path provided...Skipping')
				continue

			func = dirTree(cmd)
			
			if func != 'Invalid cmd':
				func()
			else:
				print (func)

	except:
		print ('Other Errors')
	finally:
		print ('In finally block')


