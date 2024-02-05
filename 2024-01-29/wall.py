n = int(input())
a = [int(i) for i in input().split()]

ans = [0, 0, 0]
q = 1

for i in range(n):
    if a[i] == 5:
        if q == 0:
            q = 1
    else:
        if q == 0:
            cur[1] = i + 1
            cur[2] += 5 - a[i]
        else:
            q = 0
            cur = [i + 1, i + 1, 5 - a[i]]
        if cur[2] > ans[2]:
            ans = cur.copy()
print(*ans)