inp = open("../data/10.in").read().strip().splitlines()

err = 0
inc = []
broken = []
for line in inp:
    l = []
    err0 = err
    for i in line:
        if i in ['(', '{', '[', '<']:
            l.append(i)

        elif i == ')' and l[-1] != '(':
            err += 3
            break
        elif i == ']' and l[-1] != '[':
            err += 57
            break
        elif i == '}' and l[-1] != '{':
            err += 1197
            break
        elif i == '>' and l[-1] != '<':
            err += 25137
            break
        else:
            l.pop()

    if err == err0:
        inc.append(line)
print(err)
errs = []
for line in inc:
    l = []
    for i in line:
        if i in ['(', '{', '[', '<']:
            l.append(i)
        else:
            l.pop()
    err = 0
    for i in l[::-1]:
        if i == '(':
            err *= 5
            err += 1
        if i == '[':
            err *= 5
            err += 2
        if i == '{':
            err *= 5
            err += 3
        if i == '<':
            err *= 5
            err += 4
    l.pop()
    errs.append(err)

errs.sort()
print(errs[len(errs) // 2])

