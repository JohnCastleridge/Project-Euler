import time

def find_pythagorean_triplet(sum: int) -> int:
    for a in range(1, sum//3):
        for b in range(a+1, (sum - a)//2 + 1):
            c = sum - a - b
            
            if a**2 + b**2 == c**2:
                return a*b*c


SUM=1000

start_time = time.perf_counter()

pythagorean_triplet = find_pythagorean_triplet(SUM)

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time:.4f} seconds")

print(pythagorean_triplet)