from math import sqrt, ceil

STOP = 2_000_000

def is_prime(num: int, primes: list[int]) -> bool:
    for p in primes:
        if num % p == 0:
            return False
    return True

small_primes = [2]
primes       = [2]
cut_off = ceil(sqrt(STOP))
for num in range(3, STOP+1, 2):
    if is_prime(num, small_primes):
        if num <= cut_off:
            small_primes.append(num)
        primes.append(num)

print(sum(primes))