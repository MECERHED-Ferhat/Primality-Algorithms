import sys, math
P = sys.stdin.read()


def main(p):
	if (p < 2) or (p % 2 == 0):
		return False 							# Composé

	i = 3
	BORNE = int(math.sqrt(p))

	while (i <= BORNE) and (p % i != 0):
		i += 2

	return not (i <= BORNE)

sys.stdout.write("Prime" if main(int(P)) else "Composite")
sys.stdout.flush()
sys.exit(0)