# Текстовый файл состоит не более чем из 1 200 000 символов X, Y, и Z. Определите максимальное количество идущих подряд символов, среди которых нет подстроки XZZY.

with open('6.txt') as fin:
    s = fin.read()

a = s.split('XZZY')
# print(len(max(a, key=len)) + 6)

ans = 0
for i in a:
    ans = max(ans, len(i))
print(ans + 6)