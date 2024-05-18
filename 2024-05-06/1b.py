import random
import time

n = 10000
a = [random.randint(0, 100) for i in range(n)]
# print(a)

start = time.time()
ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if (a[i] + a[j]) % 2 == 0:
            ans += 1
print(ans)
print(time.time() - start)

start = time.time()
evens = odds = 0
for i in a:
    if i % 2 == 0:
        evens += 1
    else:
        odds += 1
print(evens * (evens - 1) // 2 + odds * (odds - 1) // 2)
print(time.time() - start)

start = time.time()
evens = odds = 0
ans = 0
for i in a:
    if i % 2 == 0:
        ans += evens
        evens += 1
    else:
        ans += odds
        odds += 1
print(ans)
print(time.time() - start)