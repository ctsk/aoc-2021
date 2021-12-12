
def advance_gen(buckets):
    new = buckets[0]

    for i in range(0, len(buckets) - 1):
        buckets[i] = buckets[i + 1]

    buckets[6] += new
    buckets[8] = new

    return buckets

def simulate(initial, n_gens):
    buckets = [0] * 9

    for i in initial:
        buckets[i] += 1

    for i in range(n_gens):
        buckets = advance_gen(buckets)

    return sum(buckets)

def parse(file):
    return [int(x) for x in file.read().strip().split(",")]


def part1(inp):
    return simulate(inp, 80)


def part2(inp):
    return simulate(inp, 256)

def main():
    with open("../data/6.in", "r") as f:
        inp = parse(f)
        print(part1(inp))
        print(part2(inp))

if __name__ == "__main__":
    main()
