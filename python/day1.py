def parse(file):
    return [int(x) for x in file.read().strip().split("\n")]
 
def part1(inp):
    return sum(1 for idx in range(1, len(inp)) if inp[idx] > inp[idx - 1])
 
def part2(inp):
    return sum(1 for idx in range(3, len(inp)) if inp[idx] > inp[idx - 3])
 
def main():
    with open("../data/1.in", "r") as f:
        inp = parse(f)
        print(part1(inp))
        print(part2(inp))
 
if __name__ == "__main__":
    main()
