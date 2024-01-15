# получить список делителей числа n

n = int(input())
# a = []
# for i in range(2, n):
#     if n % i == 0:
#         a.append(i)

a = [i for i in range(2, n) if n % i == 0]

print(a)
print(sum(a))