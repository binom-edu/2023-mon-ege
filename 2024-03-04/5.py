import itertools

alf = 'капкан'
ans = set()

for i in itertools.permutations(alf):
    s = ''.join(i)
    if 'кк' not in s and 'аа' not in s:
        ans.add(s)

print(len(ans))