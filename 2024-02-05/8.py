# Определите в прилагаемом файле максимальное количество идущих подряд символов (длину непрерывной подпоследовательности), среди которых символ T встречается ровно 100 раз.

with open('8.txt') as fin:
    s = fin.read()
pos = [-1]
for i in range(len(s)):
    if s[i] == 'T':
        pos.append(i)

pos.append(len(s))

ans = 0
for i in range(len(pos) - 101):
    ans = max(ans, pos[i + 101] - pos[i] - 1)

print(ans)