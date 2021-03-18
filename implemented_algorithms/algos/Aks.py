import math, sys
P = sys.stdin.read()


def phi(n):
	# Fonction indicatrice d'Euler
	amount = 0
	for k in range(1, n + 1):
		if math.gcd(k, n) == 1:
			amount += 1
	return amount

def isPerfectPower(n):
	# Si n est une puissance parfaite -> n est composé

	for b in range(2, math.floor(math.log2(n) + 1)):
		a = n ** (1 / b)
		if a.is_integer():
			return False
	return True

def getR(n):
	# Trouvé le plus petit r tel que : Ord(r, n) > (log2 n)²

	maxK = math.floor(math.log2(n) ** 2)
	nextR = True
	r = 1

	while nextR:
		r += 1
		nextR = False
		k = 0
		while k <= maxK and not nextR:
			k = k + 1
			if pow(n, k, r) in (0, 1):
				nextR = True
	return r

def checkPgcd(n, r):
	# Si 1 < PGCD(a, n) < n pour a <= r, n est composé

	for a in range(1, r + 1):
		if 1 < math.gcd(a, n) < n:
			return False
	return True

def compareNR(n, r):
	# Si n <= r, n est premier
	return n <= r

def checkCoef(n, r):
	# Pour chaque 1 <= a <= rac(phi); Si (X + a)^n != X^n + a -> n est composé
	rn = max(math.floor(math.sqrt(phi(r)) * math.log2(n)), n)

	for a in range(1, rn):
		b = pow(a, n, n)
		if b - a != 0:
			return False

	# Sinon n est premier
	return True

def aks(n):
	if isPerfectPower(n):
		r = getR(n)
		return checkPgcd(n, r) and (compareNR(n, r) or checkCoef(n, r))
	return False

def main(p):
	if (p == 2):
		return True
	if (p < 2) and not(p & 1):
		return False

	return aks(p)

sys.stdout.write("Prime" if main(int(P)) else "Composite")
sys.stdout.flush()
sys.exit(0)