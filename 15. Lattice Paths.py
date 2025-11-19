import time

SIDE_LENGTH = 20

start_time = time.perf_counter()

grid = [[0 for _ in range(SIDE_LENGTH+1)] for _ in range(SIDE_LENGTH+1)]

grid[0][0] = 1

for row in range(SIDE_LENGTH+1):
    for col in range(SIDE_LENGTH+1):
        if row != 0:
            grid[row][col] += grid[row-1][col]
        if col != 0:
            grid[row][col] += grid[row][col-1]

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time:.4f} seconds")

print(grid[SIDE_LENGTH][SIDE_LENGTH])

