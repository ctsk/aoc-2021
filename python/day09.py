DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def parse(file):
    return [[int(x) for x in list(line)] for line in file.read().strip().splitlines()]


def isValid(x, y, height, width):
    return x >= 0 and y >= 0 and x < height and y < width

def part1(inp):
    result = 0
    height = len(inp)
    width = len(inp[0])
    for i in range(len(inp)):
        for j in range(len(inp[i])):
            is_low = True
            for (dx, dy) in DIRECTIONS:
                nx = i + dx
                ny = j + dy
                if isValid(nx, ny, height, width) and inp[nx][ny] <= inp[i][j]:
                    is_low = False
                    break
            if is_low:
                result += inp[i][j] + 1

    return result

def part2(inp):
    sizes = []
    height = len(inp)
    width = len(inp[0])
    for x in range(len(inp)):
        for y in range(len(inp[x])):
            if inp[x][y] == 9:
                continue

            open = [(x, y)]
            inp[x][y] = 9
            closed = []

            while open:
                sx, sy = open.pop()
                for (dx, dy) in DIRECTIONS:
                    nx = sx + dx
                    ny = sy + dy
                    if isValid(nx, ny, height, width) and inp[nx][ny] < 9:
                        inp[nx][ny] = 9
                        open.append((nx, ny))

                closed.append((sx, sy))
            sizes.append(len(closed))
    sizes.sort()
    return sizes[-1] * sizes[-2] * sizes[-3]

def main():
    with open("../data/9.in", "r") as f:
        inp = parse(f) 
        print(part1(inp)) 
        print(part2(inp[:]))

if __name__ == "__main__":
    main() 
