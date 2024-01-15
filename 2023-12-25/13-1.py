n = int(input())
a = []
d = 2
while d ** 2 <= n:
    if n % d == 0:
        a.append(d)
        if n // d != d:
            a.append(n // d)
    d += 1
a.sort()
print(a)