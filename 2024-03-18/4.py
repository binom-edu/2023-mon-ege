def f(x, y):
    if x > y: return x
    return y

import random, functools
n = 10
a = [random.randint(0, 1000) for i in range(n)]
print(a)

print(functools.reduce(f, a))