import random
n = 6
a = [random.randint(0, 100) for i in range(n)]
print(a)

ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if (a[i] + a[j]) % 2 == 0:
            ans += 1
print(ans)