

def d(n: int) -> int:
    proper_divisors = []
    for divisor in range(1, n//2 + 1):
        if n % divisor == 0:
            proper_divisors.append(divisor)
    return sum(proper_divisors)

sigma = 0
for a in range(1, 10_000):
    for b in range(a+1, 10_000):

        if d(a) == b and d(b) == a:
            sigma += a + b
            print(a, b)
        

print(sigma)