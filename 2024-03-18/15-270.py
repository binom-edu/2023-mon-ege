# ¬ ((x > 10) ∨ (x⋅ x < A)) ∨ ¬((y⋅y ≥  A) ∨ (y ≤ 10))
def f(x, y, a):
    ans = not(x > 10 or x ** 2 < a) or not(y ** 2 >= a or y <= 10)
    return not ans

ans = 0
for a in range(-1000, 1000):
    if all(f(x, y, a) for x in range(1, 100) for y in range(1, 100)):
        ans += 1

print(ans)