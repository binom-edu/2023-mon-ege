import random

def f(x):
    s = str(x)
    ans = 0
    for i in s:
        ans += int(i)
    return ans

n = 10
a = [random.randint(0, 1000) for i in range(n)]
print(a)

ans = a[0]
for i in a:
    if f(i) > f(ans):
        ans = i

print(ans)
print(max(a, key=f))
print(max(a, key=lambda x: sum(map(int, str(x)))))