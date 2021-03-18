from pswDep.miller_rabin import miller_rabin_base_2
from pswDep.jacobi_symbol import jacobi_symbol
from pswDep.lucas_pp import lucas_pp
from math import sqrt
import sys
P = sys.stdin.read()

def D_chooser(candidate):
	"""Choose a D value suitable for the Baillie-PSW test"""
	D = 5
	while jacobi_symbol(D, candidate) != -1:
		D += 2 if D > 0 else -2
		D *= -1
	return D

def baillie_psw(candidate):
	"""Perform the Baillie-PSW probabilistic primality test on candidate"""

	# Check divisibility by a short list of primes less than 50
	for known_prime in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]:
		if candidate == known_prime:
			return True
		elif candidate % known_prime == 0:
			return False

	# Now perform the Miller-Rabin primality test base 2
	if not miller_rabin_base_2(candidate):
		return False
		
	# Check that the number isn't a square number, as this will throw out 
	# calculating the correct value of D later on (and means we have a
	# composite number)
	# the slight ugliness is from having to deal with floating point numbers
	if int(sqrt(candidate) + 0.5) ** 2 == candidate:
		return False

	# Finally perform the Lucas primality test
	D = D_chooser(candidate)
	if not lucas_pp(candidate, D, 1, (1-D)/4):
		return False

	# You've probably got a prime!
	return True


def main(n):
	if (n == 2):
		return True
	if (n < 2 and not(n & 1)):
		return False

	return baillie_psw(n)


sys.stdout.write("Prime" if main(int(P)) else "Composite")
sys.stdout.flush()
sys.exit(0)