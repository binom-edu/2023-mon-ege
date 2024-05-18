import sys, itertools
sys.stdin = open('27424a.txt')

n = int(input())
a = []
for i in range(n):
    a.append([int(j) for j in input().split()])

ans = 0
for i in itertools.product([0, 1], repeat=n):
    s = 0
    for j in range(n):
        var = i[j]
        s += a[j][var]
    if s % 3 != 0 and s > ans:
        ans = s
print(ans)