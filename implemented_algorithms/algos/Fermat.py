import random, math, sys
P = sys.stdin.read()

dice = random.SystemRandom()
PRECISION = 20
 
def get_coprime(n):
    while True:
        coprime = dice.randrange(0, n)
        if math.gcd(coprime, n) == 1:
            return coprime
 
 
def fermat_primality(n):
    for _ in range(PRECISION):
        a = get_coprime(n)
        if pow(a, n-1, n) != 1:
            return False
    return True

def main(n):
	if (n == 2):
		return True
	if (n < 2 or not(n & 1)):
		return False

	return fermat_primality(n)


sys.stdout.write("Prime" if main(int(P)) else "Composite")
sys.stdout.flush()
sys.exit(0)