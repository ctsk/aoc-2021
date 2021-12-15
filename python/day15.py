from queue import PriorityQueue

def parse(file):
    return [list(map(int, list(line))) for line in file.read().splitlines()]

DIR = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def isValid(x, y, height, width):
    return x >= 0 and y >= 0 and x < height and y < width

def shortestPaths(grid, start, cost_function, repeat=1):
    q = PriorityQueue()
    height, width = repeat * len(grid), repeat * len(grid[0])
    mv = height * width * 10
    d = [[mv for _ in range(width)] for _ in range(height)]

    start_x, start_y = start
    q.put((0, start_x, start_y))
    d[start_x][start_y] = 0

    while not q.empty():
        dist, pos_x, pos_y = q.get()
        for dx, dy in DIR:
            nx = pos_x + dx
            ny = pos_y + dy
            if not isValid(nx, ny, height, width):
                continue

            cost = cost_function(nx, ny)
            if dist + cost < d[nx][ny]:
                d[nx][ny] = d[pos_x][pos_y] + cost
                q.put((d[nx][ny], nx, ny))

    return d

def part1(inp):
    def cost(nx, ny):
        return inp[nx][ny]
    return shortestPaths(inp, (0, 0), cost)[-1][-1]

def part2(inp):
    def cost(nx, ny):
        height, width = len(inp), len(inp[0])
        repeat_x, repeat_y= nx // height, ny // width
        val = inp[nx % height][ny % width] + repeat_x + repeat_y
        looped_val = ((val - 1) % 9) + 1
        return looped_val

    return shortestPaths(inp, (0, 0), cost, repeat=5)[-1][-1]


with open("../data/15.in", "r") as f:
    inp = parse(f)
    print(part1(inp))
    print(part2(inp))
