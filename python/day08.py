
def c2b(c):
    return 1 << (ord(c) - ord('a'))

def w2b(w):
    r = 0
    for c in w:
        r |= c2b(c)
    return r

def dec(bw, d):
    cl = bw.bit_count()
    c1 = (d[0] & bw).bit_count() == 2
    c4 = (d[1] & bw).bit_count() == 3

    if cl == 5:
        if c1:
            return 3
        else:
            if c4:
                return 5
            else:
                return 2
    elif cl == 6:
        if c1:
            if c4:
                return 0
            else:
                return 9
        else:
            return 6

def parse(file):
    inp0 = file.read().strip().splitlines()
    inp1 = [x.split(" | ") for x in inp0]
    inp2 = [(x[0].split(" "), x[1].split(" ")) for x in inp1]
    return inp2

def part1(inp):
    target_lengths = [2, 3, 4, 7]

    result = 0
    for line in inp:
        for w in line[1]:
            if len(w) in target_lengths:
                result += 1
    return result

def part2(inp):
    result = 0
    for line in inp:
        obs = [ w2b(w) for w in line[0] ]
        res = [ w2b(w) for w in line[1] ]

        d = [0] * 2
        obs1 = []
        m = {}
        for bw in obs:
            match bw.bit_count():
                case 2:
                    d[0] = bw
                    m[bw] = 1
                case 3:
                    m[bw] = 7
                case 4:
                    d[1] = bw
                    m[bw] = 4
                case 7:
                    m[bw] = 8
                case _:
                    obs1.append(bw)

        for bw in obs1:
            m[bw] = dec(bw, d)

        
        result += m[res[0]] * 1000 + m[res[1]] * 100 + m[res[2]] * 10 + m[res[3]]
    return result

def main():
    with open("../data/8.in", "r") as f:
        inp = parse(f)
        print(part1(inp))
        print(part2(inp))

if __name__ == "__main__":
    main()
