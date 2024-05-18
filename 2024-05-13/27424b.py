import sys
sys.stdin = open('27424b.txt')

n = int(input())
a = []
for i in range(n):
    a.append([int(j) for j in input().split()])

ans = 0
min_d = 10 ** 12
for p in a:
    ans += max(p)
    if p[0] % 3 != p[1] % 3:
        min_d = min(min_d, max(p) - min(p))
if ans % 3 != 0:
    print(ans)
else:
    print(ans - min_d)