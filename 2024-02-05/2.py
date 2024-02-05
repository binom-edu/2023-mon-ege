# Найдите длину самой длинной подцепочки, состоящей из символов Y

with open('2.txt') as fin:
    s = fin.read()

ans = 0
while 'Y' * ans in s:
    ans += 1

print(ans - 1)