import random
n = 10
a = [random.randint(0, 1000) for i in range(n)]
print(a)

ans = a[0]
for i in a:
    if i > ans:
        ans = i

print(ans)
print(max(a))