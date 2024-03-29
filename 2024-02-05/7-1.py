# Определите максимальное количество идущих подряд пар символов AB или CB в прилагаемом файле.

# Искомая подпоследовательность должна состоять только из пар AB, или только из пар CB, или только из пар AB и CB в произвольном порядке следования этих пар.

with open('7.txt') as fin:
    s = fin.read().replace('AB', '*').replace('CB', '*')

ans = 0
while '*' * ans in s:
    ans += 1
print(ans - 1)