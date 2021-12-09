def parse(file):
    return file.read().strip().splitlines()

def part1(data):
    gamma = ''
    eps = ''

    for pos in zip(*data):
        if pos.count('1') > pos.count('0'):
            gamma += '1'
            eps += '0'
        else:
            gamma += '0'
            eps += '1'

    return int(gamma, 2) * int(eps, 2)

def part2(data):
    def helper(data, pos, bit):
        if (len(data) <= 1):
            return data
        
        bits = [line[pos] for line in data]
        
        if (bit == 1):
            common = 1 if bits.count('1') >= bits.count('0') else 0
        if (bit == 0):
            common = 1 if bits.count('1') < bits.count('0') else 0

        new_data = [line for line in data if line[pos] == str(common)]
        return helper(new_data, pos + 1, bit)

    oxygen = helper(data, 0, 1)
    co2 = helper(data, 0, 0)
    return int(oxygen[0], 2) * int(co2[0], 2)

def main():
    with open("../data/3.in", "r") as f:
        inp = parse(f)
        print(part1(inp))
        print(part2(inp))
 
if __name__ == "__main__":
    main()    



        
