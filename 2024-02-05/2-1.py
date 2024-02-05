# Найдите длину самой длинной подцепочки, состоящей из символов Y

with open('2.txt') as fin:
    s = fin.read()

cur = ans = 0
for i in s:
    if i == 'Y':
        cur += 1
        ans = max(ans, cur)
    else:
        cur = 0
print(ans)