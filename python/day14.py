from math import ceil
from collections import Counter, defaultdict

PART_1_ITERATIONS = 10
PART_2_ITERATIONS = 40

def parse(file):
    lines = file.read().strip().splitlines()
    div = lines.index("")
    initial = lines[0]
    rules = { line[:2] : (line[0] + line[6], line[6] + line[1]) for line in lines[(div + 1):] }
    return initial, rules

def naive_produce(string, rules):
    res = [ string[0] ]
    for idx in range(1, len(string)):
        right_char = string[idx]
        pair = string[idx - 1: idx + 1]
        if derivs := rules.get(pair, None):
            res.append(derivs[1])
        else:
            res.append(right_char)
    return ''.join(res)

def smart_produce(pair_count, rules):
    new_pair_count = defaultdict(int)
    for pair, count in pair_count.items():
        deriv1, deriv2 = rules[pair]
        new_pair_count[deriv1] += count
        new_pair_count[deriv2] += count

    return new_pair_count

def part1(initial, rules):
    working_string = initial
    for _ in range(PART_1_ITERATIONS):
        working_string = naive_produce(working_string, rules)

    counts = Counter(working_string).most_common()
    most_common_count = counts[0][1]
    least_common_count = counts[-1][1]
    return most_common_count - least_common_count

def ceil_half(n):
    if n % 2 == 0:
        return n // 2
    else:
        return (n - 1) // 2 + 1

def part2(initial, rules):
    pair_count = defaultdict(int)
    new_pair_count = defaultdict(int)

    for idx in range(1, len(initial)):
        pair = initial[idx - 1 : idx + 1]
        pair_count[pair] += 1

    for _ in range(PART_2_ITERATIONS):
        pair_count = smart_produce(pair_count, rules)

    char_count = defaultdict(int)
    for pair, count in pair_count.items():
        char_count[pair[0]] += count
        char_count[pair[1]] += count

    char_count = sorted([(ceil_half(count), char) for char, count  in char_count.items()])
    return char_count[-1][0] - char_count[0][0]

def main():
    with open("../data/14.in", "r") as f:
        inp = parse(f)
        print(part1(*inp))
        print(part2(*inp))

if __name__ == "__main__":
    main()
