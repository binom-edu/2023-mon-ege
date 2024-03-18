def p(x):
    return 8 <= x <= 16
def q(x):
    return 25 <= x <= 40
def a(x):
    return l <= x <= r

def f(x):
    return not(p(x) or q(x)) or a(x)

ans = 100
for l in range(100):
    for r in range(100):
        if all(f(x) for x in range(100)):
            ans = min(ans, r - l)
print(ans)