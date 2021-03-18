import sys
from random import *
P = sys.stdin.read()

PRECISION = 20

def main(n):

    # If number is even, it's a composite number
    if n == 2:
        return True

    if (n < 2) or (n % 2) == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(PRECISION):
        a = randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

sys.stdout.write("Prime" if main(int(P)) else "Composite")
sys.stdout.flush()
sys.exit(0)