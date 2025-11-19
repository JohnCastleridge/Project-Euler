import time

STOP = 20

def is_prime(num: int, primes: list[int]) -> bool:
    for p in primes:
        if num % p == 0:
            return False
    return True

start_time = time.perf_counter()

prime_conter = {}
for num in range(2, STOP+1):
    if is_prime(num, prime_conter.keys()):
        prime_conter[num] = 0

    for prime in prime_conter:
        multiplicity = 0
        while num % prime**(multiplicity+1) == 0:
            multiplicity += 1
        prime_conter[prime] = max(prime_conter[prime], multiplicity)

product = 1
for prime, multiplicity in prime_conter.items():
    product *= prime**multiplicity


end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time:.4f} seconds")

print(product)

