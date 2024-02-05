# Текстовый файл состоит не более чем из 1 200 000 символов X, Y, и Z. Определите максимальное количество идущих подряд символов, среди которых нет подстроки XZZY.

with open('6.txt') as fin:
    s = fin.read()

cur = ans = 4
for i in range(4, len(s)):
    if s[i - 3: i + 1] != 'XZZY':
        cur += 1
        ans = max(ans, cur)
    else:
        cur = 3

print(ans)