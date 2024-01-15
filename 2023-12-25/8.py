# все положительные элементы возвести в квадрат
import random
a = [random.randint(-10, 10) for i in range(10)]
print(a)
for i in range(len(a)):
    if a[i] > 0:
        a[i] = a[i] ** 2
print(a)

print('---')
for i in a:
    i = i ** 2

print(a)