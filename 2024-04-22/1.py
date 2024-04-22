import random
n = 10
a = [random.randint(0, 100) for i in range(n)]
print('a:', a)

b = sorted(a)
print('a:', a)
print('b:', b)

a.sort()
print('a:', a)