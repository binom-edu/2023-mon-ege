a = [i for i in range(2, 6)]
print(a)
a = [i ** 2 for i in range(10)]
print(a)
b = [i for i in a if i % 10 == 9]
print(b)