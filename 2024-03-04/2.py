import itertools

alf = 'abc'

for ind, i in enumerate(itertools.product(alf, repeat=5)):
    s = ''.join(i)
    print(ind + 1, s)
    if s == 'ccaba':
        ans = ind + 1

print(ans)