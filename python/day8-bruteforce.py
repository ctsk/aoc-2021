inp0 = open("input.txt").read().strip().splitlines()
inp1 = [x.split(" | ") for x in inp0]
inp = [(x[0].split(" "), x[1].split(" ")) for x in inp1]

c = 0
for line in inp:
    out = line[1]

    for word in out:
        if len(word) in [2, 3, 4, 7]:
            c += 1

allowed = [
    'abcefg', 'cf', 'acdeg',
    'acdfg', 'bcdf', 'abdfg',
    'abdefg', 'acf', 'abcdefg',
    'abcdfg'
]

def trans(word, mapping):
    w2 = ""
    for c in word:
        x = mapping[ord(c) - ord('a')]
        w2 += x
    m = list(w2)
    m.sort()

    return ''.join(m)

def isValid(word, mapping):
    return trans(word, mapping) in allowed

import itertools as it
cs = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

perms = [('c', 'f', 'g', 'a', 'b', 'd', 'e')]
r = 0
for line in inp:
    i = line[0]
    o = line[1]
    for perm in it.permutations(cs):
        flag = True
        for word in i + o:
            if not isValid(word, perm):
                flag = False
                break
        if (flag):
            s = ''
            for word in o:
                t = trans(word, perm)
                s += str(allowed.index(t))

            print(int(s))
            r += int(s)
            break

print(r)
