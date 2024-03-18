import random
n = 4
a = [random.randint(-1, 10) for i in range(n)]
print(a)

# Правда ли, что все элементы a положительные
print(all(i > 0 for i in a))