import sys
P = sys.stdin.read()

def isFermat(n):
	i = 0
	result = 3
	while (result < n):
		i += 1
		result = (2 << ((2 << i) - 1)) + 1

	return (result == n)

def isFermatPrime(n):
	if (isFermat(n)):
		return pow(3, (n-1) >> 1, n) == (n - 1)
	return False

def main(n):
	if (n in (3, 5)):
		return True
	if (n < 17 or not(n & 1)):
		return False

	return isFermatPrime(n)

sys.stdout.write("Fermat Prime" if main(int(P)) else "Not Fermat Prime")
sys.stdout.flush()
sys.exit(0)