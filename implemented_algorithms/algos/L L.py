import sys
import math
P = sys.stdin.read()


def main(p):
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

	try:
		# runs through test until interrupted
		# checks if power is a Fermat psuedoprime
		if fermat(p) == True or p == 3 or p == 5:
			value = 2 ** p - 1
			# checks if value is a Mersenne prime
			if getLucas(p - 1, value) == 0:
				return True
		return False
	except Exception as e:
		pass

sys.stdout.write("Mersenne Prime" if main(int(P)) else "Not Mersenne Prime")
sys.stdout.flush()
sys.exit(0)