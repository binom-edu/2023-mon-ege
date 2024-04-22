import sys
sys.stdin = open('kurs26-2.txt')

n, k = map(int, input().split())
a = []
for i in range(n):
    weight, price = map(int, input().split())
    a.append([weight, price])

a.sort(key=lambda x: [x[1] / x[0], -x[0]])

ans1 = 0
for i in a[:k]:
    ans1 += i[0]

print(ans1)
print(max(a[:k])[1])