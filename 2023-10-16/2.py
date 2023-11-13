# перестановки
# посчитать количество перестановок, в которых встречается no
import itertools

ans = 0
alf = 'binom'
for p in itertools.permutations(alf):
    s = ''.join(p)
    if 'no' in s:
        ans += 1

print(ans)