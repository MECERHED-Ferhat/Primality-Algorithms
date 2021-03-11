# imports necessary modules
from math import log
from time import time
from random import randint

# returns current lucas number
def getLucas(index, modulo):
	prev = 4
	for x in range(1,index):
		prev = ( prev ** 2 - 2 ) % modulo
	return prev

# tests to see if p passes Fermat's Little Theorem
def fermat(p):
	testPass = 0
	for a in range (2,7):
		if (a ** (p - 1)) % p == 1:
			testPass += 1
	if testPass == 5:
		return True
	else:
		return False

# gets time elapsed since last prime was found
def getTime(start):
	total = time() - start
	hours = int(total / 3600)
	total = total % 3600
	minutes = int(total / 60)
	seconds = int(total % 60)
	print(str(hours) + "h " + str(minutes) + "m " + str(seconds) + "s elapsed since last Mersenne Prime found\n")
	return time()
	
# checks to see if a given number passes the Lucas-Lehmer Test
try:
	power = 3
	print("M(2)\n3\n")
	start = time()
	start = getTime(start)
	
	# runs through test until interrupted
	while True:
		
		# checks if power is a Fermat psuedoprime
		if fermat(power) == True or power == 3 or power == 5:
			value = 2 ** power - 1
			
			# checks if value is a Mersenne prime
			if getLucas(power - 1, value) == 0:
				print("M(" + str(power) + ")\n" + str(value) + "\n")
				start = getTime(start)
		power += 2
		
# stops program if interrupted by keyboard
except KeyboardInterrupt:
	pass