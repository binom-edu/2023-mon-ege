import random
a = [random.randint(-10, 10) for i in range(10)]
print(a)
for i in range(len(a)):
    print(a[i])

print('---')
for i in a:
    print(i)