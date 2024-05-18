import sys
sys.stdin = open('27989_B.txt')

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

n26 = n2 = n13 = n1 = 0
for i in a:
    if i % 26 == 0:
        n26 += 1
    elif i % 13 == 0:
        n13 += 1
    elif i % 2 == 0:
        n2 += 1
    else:
        n1 += 1

print(n26 * (n26 - 1) // 2 + n26 * (n2 + n13 + n1) + n13 * n2)