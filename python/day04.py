class Board():
    def __init__(self, nums):
        self.nums = nums
        self.num2pos = {}
        self.height = len(nums)
        self.width  = len(nums[0])
        self.mark = [ [False for _ in range(self.width)] for _ in range(self.height)]

        for i in range(self.height):
            for j in range(self.width):
                self.num2pos[int(nums[i][j])] = (i, j)

    def set(self, num):
        if num not in self.num2pos:
            return False

        (row, col) = self.num2pos[num]
        self.mark[row][col] = True
        return self.check_row(row) or self.check_col(col)

    def check_row(self, row):
        for i in self.mark[row]:
            if not i:
                return False
        return True

    def check_col(self, col):
        for i in self.mark:
            if not i[col]:
                return False
        return True

    def print(self):
        for row in self.nums:
            for col in row:
                print(col, end=' ')
            print()

    def sum_unmarked(self):
        sum = 0
        for i in range(self.height):
            for j in range(self.width):
                if not self.mark[i][j]:
                    sum += int(self.nums[i][j])
        return sum

def parse(file):
    inp = open("../data/4.in").read().strip().split("\n\n")
    callouts = [int(x) for x in inp[0].strip().split(",")]
    boards = []
    
    for i in inp[1:]:
        boards.append(Board([line.split() for line in i.splitlines()]))

    return callouts, boards

def part1(inp):
    callouts, boards = inp
    for callout in callouts:
        for board in boards:
            if board.set(callout):
                return board.sum_unmarked() * callout

def part2(inp):
    callouts, boards = inp
    winners = 0
    won = {board : False for board in boards}
    for callout in callouts:
        for board in boards:
            if not won[board] and board.set(callout):
                winners += 1
                won[board] = True
            if winners == len(boards):
                return board.sum_unmarked() * callout

def main():
    with open("../data/4.in", "r") as f:
        inp = parse(f)
        print(part1(inp))
        print(part2(inp))
 
if __name__ == "__main__":
    main()
