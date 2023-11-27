def r(n):
    s = bin(n)[2:]
    for i in range(2):
        cnt = s.count('1')
        s = s + str(cnt % 2)
    return int(s, 2)

n = 1
while r(n) <= 77:
    n += 1
    print(n, r(n)) # чтобы душа была спокойна

print(n, r(n))