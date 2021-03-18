from random import randint
import sys

P = sys.stdin.read()

PRECISION = 20

def prime_factors(n):
	i = 2
	factors = []
	while i * i <= n:
		if n % i:
			i += 1
		else:
			n //= i
			factors.append(i)
	if n > 1:
		factors.append(n)
	return factors

def is_probably_prime(n):

	if n < 3 or not n % 2:
		return number == 2

	for _ in range(PRECISION):

		a = randint(2, n - 1)

		if pow(a, n - 1, n) != 1:
			return False

		p_factors = prime_factors(n - 1)

		for q in p_factors:
			if pow(a, (n - 1)//q, n) == 1:
				break

		else:
			return True

	return False

def main(n):
	if (n == 2):
		return True
	if (n < 2 or not(n & 1)):
		return False

	return is_probably_prime(n)


sys.stdout.write("Prime" if main(int(P)) else "Composite")
sys.stdout.flush()
sys.exit(0)