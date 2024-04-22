import random
n = 10
a = [random.randint(0, 100) for i in range(n)]
print('a:', a)

a.sort(reverse=True)
print('a:', a)