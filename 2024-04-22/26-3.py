import sys
sys.stdin = open('kurs26-3.txt')

n, s = map(int, input().split())

a = []
for i in range(n):
    t = input().split()
    a.append([t[0], int(t[1]), int(t[2])])

a.sort(key=lambda x: [x[0], -x[1]], reverse=True)

ans1 = 0
for x in a:
    cnt = min(x[2], s // x[1])
    if x[0] == 'A':
        ans1 += cnt
    s -= cnt * x[1]
print(ans1, s)