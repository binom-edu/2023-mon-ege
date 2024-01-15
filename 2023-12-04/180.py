def f(n):
    ans = 0
    for i in range(8):
        ans |= (not(n >> i & 1)) << i

    return ans + 1

    b = bin(n)[2:].rjust(8, '0')
    b1 = ''
    for i in b:
        if i == '0':
            b1 += '1'
        else:
            b1 += '0'
    return int(b1, 2) + 1

for i in range(128):
    if f(i) == 153:
        print(i)
        break