SIDE_LENGTH = 20

grid = [[0 for _ in range(SIDE_LENGTH+1)] for _ in range(SIDE_LENGTH+1)]

grid[0][0] = 1

for row in range(SIDE_LENGTH+1):
    for col in range(SIDE_LENGTH+1):
        if row != 0:
            grid[row][col] += grid[row-1][col]
        if col != 0:
            grid[row][col] += grid[row][col-1]


print(grid[SIDE_LENGTH][SIDE_LENGTH])
