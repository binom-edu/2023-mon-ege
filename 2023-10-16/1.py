# перестановки
import itertools

num = 1
alf = 'binom'
for p in itertools.permutations(alf):
    s = ''.join(p)
    print(num, s)
    num += 1