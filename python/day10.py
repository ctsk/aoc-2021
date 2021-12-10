def parse(file):
    return file.read().strip().splitlines()

opn = frozenset(('(', '{', '[', '<'))
clos = frozenset((')', '}', ']', '>'))

penalty = {
   ')': 3,
   '}': 57,
   ']': 1197,
   '>': 25137
}

score = {
   '(': 1,
   '{': 2,
   '[': 3,
   '<': 4
}

complementary = {
   ')': '(',
   '}': '{',
   ']': '[',
   '>': '<'
}

def calculate_correction(opn_stack):
    correction = 0
    for char in opn_stack[::-1]:
        correction *= 5
        correction += score[char]
    return correction

def part_1_and_2(inp):
    error_score = 0
    correction_scores = []
    for line in inp:
        stack = []
        error_before_line = error_score
        for char in line:
            if char in opn:
                stack.append(char)
            elif char in clos:
                if stack[-1] == complementary[char]:
                    stack.pop()
                else:
                    error_score += penalty[char]
                    break
        if (error_score == error_before_line):
            correction_scores.append(calculate_correction(stack))
    correction_scores.sort()
    return error_score, correction_scores[len(correction_scores) // 2]

def main():
    with open("../data/10.in", "r") as f:
        inp = parse(f)
        p1, p2 = part_1_and_2(inp)
        print(p1)
        print(p2)

if __name__ == "__main__":
    main()
