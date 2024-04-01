import itertools

alf = 'школа'

ans = 0
for i in itertools.product(alf, repeat=3):
    if i.count('к') == 1:
        ans += 1
print(ans)