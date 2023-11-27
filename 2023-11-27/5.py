def f(n):
    d1 = n % 10
    d2 = n // 10 % 10
    d3 = n // 100
    mn = min(d1, d2, d3)
    mx = max(d1, d2, d3)
    md = d1 + d2 + d3 - mx - mn
    maxx = mx * 10 + md
    if mn == md == 0:
        mn = mx
    elif mn == 0:
        mn, md = md, mn
    minx = mn * 10 + md
    return maxx - minx

n = 100
while f(n) != 40:
    n += 1
print(n)