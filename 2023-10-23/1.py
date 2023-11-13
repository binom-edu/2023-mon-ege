import itertools

primes = '2357b'

ans = 0
alf = '0123456789ab'
for i in itertools.combinations_with_replacement(alf, 8):
    cnt = 0
    for j in primes:
        cnt += i.count(j)
    if i[0] != '0' and cnt >= 2 and int(i[0], 12) % 2 != int(i[-1], 12) % 2:
        ans += 1
        print(i)

print(ans)