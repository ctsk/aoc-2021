def parse(file):
    lines = file.read().strip().splitlines()
    divider = lines.index("")
    dotsLists = [line.split(",") for line in lines[:divider]]
    dots = set((int(dot[0]), int(dot[1])) for dot in dotsLists)
    axes = [(line[11], int(line[13:])) for line in lines[(divider + 1):]]

    return dots, axes

def mirror(dot, axis):
    x, y = dot
    dir, pos = axis
    if dir == 'x' and x > pos:
        return 2 * pos - x, y
    elif dir == 'y' and y > pos:
        return x, 2 * pos - y
    else:
        return x, y

def fold(dots, axis):
    return {mirror(dot, axis) for dot in dots}

def part1(dots, axes):
    return fold(dots, axes[0])

def part2(dots, axes):
    d = dots
    for axis in axes:
        d = fold(d, axis)
    return d

def print_dots(dots):
    x_min = min(x for x, _ in dots)
    y_min = min(y for _, y in dots)
    x_max = max(x for x, _ in dots) + 1
    y_max = max(y for _, y in dots) + 1
    for y in range(y_min, y_max):
        print("".join("#" if (x, y) in dots else " "
                    for x in range(x_min, x_max)))

def main():
    with open("../data/13.in", "r") as f:
        dots, axes = parse(f)
        print(len(part1(dots, axes)))
        print_dots(part2(dots, axes))


if __name__ == "__main__":
    main()
