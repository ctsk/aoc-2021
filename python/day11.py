DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
GRID_SIZE = 10

def parse(file):
    return [[int(x) for x in list(line)] for line in file.read().strip().splitlines()]

def isValid(x, y):
    return x >= 0 and y >= 0 and x < GRID_SIZE and y < GRID_SIZE

def start_chain(grid, row, col, safe):
    for x, y in DIRECTIONS:
        nx = x + row
        ny = y + col
        if (isValid(nx, ny)) and (nx, ny) not in safe:
            grid[nx][ny] += 1
            if grid[nx][ny] > 9:
                safe.add((nx, ny))
                start_chain(grid, nx, ny, safe)
    grid[row][col] = 0

def next_gen(grid):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            grid[row][col] += 1

    safe = set()
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row][col] > 9 and (row, col) not in safe:
                safe.add((row, col))
                start_chain(grid, row, col, safe)
    return len(safe)


def print_grid(grid):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row][col] == 0:
                print('.', end = '')
            elif grid[row][col] > 9:
                print('+', end = '')
            else:
                print(grid[row][col], end = '')
        print()
    print()

grid = parse(open("../data/11.in"))
gen = 0
total_flashes = 0
while True:
    flashes = next_gen(grid)
    total_flashes += flashes
    gen += 1
    if (flashes == GRID_SIZE * GRID_SIZE):
        print(f"(Part 2) {gen}")
        break
    if gen == 100:
        print(f"(Part 1) {total_flashes}")

