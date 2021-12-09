def parse(file):
    return [int(x) for x in file.read().strip().split(",")]

def odd_median(x):
    x.sort()
    return x[len(x) // 2]

def part1(inp):
    med = odd_median(inp)
    return sum(abs(x - med) for x in inp)

def part2(inp):
    mean = sum(inp) // len(inp)
    distances = [abs(x - mean) for x in inp]
    return sum(x * (x + 1) // 2 for x in distances)

def main():
    with open("../data/7.in", "r") as f:
        inp = parse(f)
        print(part1(inp))
        print(part2(inp))

if __name__ == "__main__":
    main()
