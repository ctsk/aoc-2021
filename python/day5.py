import re


def parse(file):
    numbers_re = re.compile(r'\d+')
    inp = file.read().strip().splitlines()
    pipes = []
    for line in inp:
        x1, y1, x2, y2 = numbers_re.findall(line)
        pipes.append(((int(x1), int(y1)), (int(x2), int(y2))))
    return pipes

def signum(x):
    if x == 0:
        return 0
    if x > 0:
        return 1
    else:
        return -1


def lay_pipe(x1, y1, x2, y2, grid):
    dx = x2 - x1
    dy = y2 - y1
    distance = max(abs(dx), abs(dy)) + 1

    dir_x = signum(dx)
    dir_y = signum(dy)

    for i in range(distance):
        new = x1 + i * dir_x , y1 + i * dir_y
        grid[new] =  grid.get(new, 0) + 1


def part1(inp):
    grid = {}

    for ((x1, y1), (x2, y2)) in inp:
        if x1 == x2 or y1 == y2:
            lay_pipe(x1, y1, x2, y2, grid)

    return sum(1 for x in grid.values() if x > 1)

def part2(inp):
    grid = {}
    for ((x1, y1), (x2, y2)) in inp:
        lay_pipe(x1, y1, x2, y2, grid)

    return sum(1 for x in grid.values() if x > 1)

def main():
    with open("../data/5.in", "r") as f:
        inp = parse(f)
        print(part1(inp))
        print(part2(inp))
 
if __name__ == "__main__":
    main()
