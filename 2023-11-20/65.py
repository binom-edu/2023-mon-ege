maxx = cnt = 0
for x in range(8800, 55535 + 1):
    s = str(x)
    prod = 1
    for i in s:
        prod *= int(i)
    if '7' in s and prod > 35:
        cnt += 1
        maxx = x
    # prod = 1
    # n = x
    # has7 = False
    # while n > 0:
    #     d = n % 10
    #     prod *= d
    #     if d == 7:
    #         has7 = True
    #     n //= 10
    # if has7 and prod > 35:
    #     cnt += 1
    #     maxx = x
print(maxx, cnt)