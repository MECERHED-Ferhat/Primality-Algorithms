import random
import sys

P = sys.stdin.read()



dice = random.SystemRandom()
PRECISION = 20

def isProth(p):
	k = 1
	exp = 2
	while (exp*k + 1 < p):
		k += 1
		if (k >= exp):
			exp <<= 1
			k = 1
	return (exp*k + 1 == p)

def isProthPrime(p):
	global PRECISION
	
	for i in range(PRECISION):
		a = dice.randrange(2, p)
		rst = pow(a, (p-1) >> 1, p)
		if (rst == p-1):
			return True
		if (rst**2 != 1):
			return False
		if (rst != -1) and (rst != 1) and (rst**2 == 1):
			return False

	return False

def main(p):
	if (p <= 2) or not(p & 1):
		return False

	return isProth(p) and isProthPrime(p)



sys.stdout.write("Proth Prime" if main(int(P)) else "Not Proth Prime")
sys.stdout.flush()
sys.exit(0)