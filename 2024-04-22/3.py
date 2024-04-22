import random
n = 10
a = [random.randint(0, 100) for i in range(n)]
print('a:', a)

def f(x):
    ans = 0
    while x > 0:
        ans += x % 10
        x //= 10
    return ans

a.sort(key=f)
print('a:', a)

a.sort(key=lambda x: sum(map(int, str(x))))
print('a:', a)