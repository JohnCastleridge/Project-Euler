from math import isqrt
import time

STOP = 2_000_000

def is_prime(num: int, primes: list[int]) -> bool:
    cut_off = isqrt(num)+1
    for p in primes:
        if p > cut_off:
            break
        if num % p == 0:
            return False
    return True

start_time = time.perf_counter()

primes = [2]
for num in range(3, STOP+1, 2):
    if is_prime(num, primes):
        primes.append(num)

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time:.4f} seconds")

print(sum(primes))|1