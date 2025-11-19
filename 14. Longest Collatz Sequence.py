import time

STOP = 1_000_000


def next(n: int) -> int:
    mod = n % 2
    if mod == 0:
        return n // 2
    if mod == 1:
        return 3*n + 1

start_time = time.perf_counter()

distance_map= {1:0}
longest_distance = 0
longest_start = 1
for start in range(2, STOP + 1):
    branch = []
    num = start
    # Iterate until we find a cached value
    while num not in distance_map:
        branch.append(num)
        num = next(num)
    
    # Backfill lengths for the branch
    length = distance_map[num]
    for key in reversed(branch):
        length += 1
        distance_map[key] = length
    
    # Store the best value
    if distance_map[start] > longest_distance:
        longest_distance = distance_map[start]
        longest_start    = start


end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time:.4f} seconds")

print(longest_start)

