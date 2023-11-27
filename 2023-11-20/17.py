with open('17.txt') as fin:
    a = [int(i) for i in fin]

n = len(a)

cnt = 0
maxs = - 10 ** 9
for i in range(n - 1):
    x, y = a[i], a[i + 1]
    if x % 3 == 0 or y % 3 == 0:
        cnt += 1
        maxs = max(maxs, x + y)
print(cnt, maxs)