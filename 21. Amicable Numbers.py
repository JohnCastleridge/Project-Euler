import time


def d(n: int) -> int:
    proper_divisors = []
    for divisor in range(1, n//2 + 1):
        if n % divisor == 0:
            proper_divisors.append(divisor)
    return sum(proper_divisors)

start_time = time.perf_counter()

sigma = 0
for a in range(1, 10_000):
    b = d(a)
    if b == a:
        continue

    if d(b) == a:
        sigma += a + b
        
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time:.4f} seconds")

print(sigma//2)