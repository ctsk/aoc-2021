def parse(file):
    x = [line.split() for line in file.read().strip().splitlines()]
    y = [(a[0], int(a[1])) for a in x]
    return y


def part1(inp):
    d = 0
    f = 0
    for (op, dist) in inp:
        if op == 'forward':
            f += dist
        elif op == 'up':
            d -= dist
        elif op == 'down':
            d += dist
    return d * f

def part2(inp):
    aim = 0
    d = 0
    f = 0
    for (op, dist) in inp:
        if op == 'forward':
            f += dist
            d += aim * dist
        elif op == 'up':
            aim -= dist
        elif op == 'down':
            aim += dist
    return d * f

def main():
    with open("../data/2.in", "r") as f:
        inp = parse(f)
        print(part1(inp))
        print(part2(inp))

if __name__ == "__main__":
    main()
