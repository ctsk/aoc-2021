import numpy as np

n = 9
m = np.zeros(shape=(9, 9))

m[6, 0] = 1
for i in range(n):
    m[i,(i + 1) % n] = 1

inp = [int(x) for x in open("input.txt").read().strip().split(",")]
x = np.zeros(shape=(9, 1))

for i in inp:
    x[i] += 1

print(x)
print(np.linalg.matrix_power(m, 2))
print(np.sum(np.dot(np.linalg.matrix_power(m, 256), x)))


