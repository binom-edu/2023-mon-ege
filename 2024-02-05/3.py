# Определите максимальное количество идущих подряд символов, среди которых каждые два соседних различны
with open('3.txt') as fin:
    s = fin.read()

cur = ans = 1
for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        cur += 1
        ans = max(ans, cur)
    else:
        cur = 1
print(ans)