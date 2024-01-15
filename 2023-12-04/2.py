def r(n):
    b = bin(n)[2:]
    if n % 3 == 0:
        b += b[-3:]
    else:
        b += bin((n % 3) * 3)[2:]
    return int(b, 2)

n = 4
while r(n) < 76:
    n += 1

print(n, r(n))