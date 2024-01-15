def f(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return f(n // 2) - 1
    return 3 + f(n - 1)

ans = set()
for i in range(1000):
    ans.add(f(i))

print(len(ans))