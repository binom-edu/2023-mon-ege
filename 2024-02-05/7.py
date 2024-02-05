# Определите максимальное количество идущих подряд пар символов AB или CB в прилагаемом файле.

# Искомая подпоследовательность должна состоять только из пар AB, или только из пар CB, или только из пар AB и CB в произвольном порядке следования этих пар.

with open('7.txt') as fin:
    s = fin.read()

cur = ans = 0
for i in range(1, len(s), 2):
    if s[i] == 'B' and (s[i - 1] == 'A' or s[i - 1] == 'C'):
        cur += 1
        ans = max(ans, cur)
    else:
        cur = 0

cur = 0
for i in range(2, len(s), 2):
    if s[i] == 'B' and (s[i - 1] == 'A' or s[i - 1] == 'C'):
        cur += 1
        ans = max(ans, cur)
    else:
        cur = 0
print(ans)