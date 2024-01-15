def f(n):
    global ans
    ans += 1
    if n >= 1:
        ans += 1
        f(n - 1)
        f(n - 2)

ans = 0

f(28)
print(ans)