import sys
sys.stdin = open('57434a.txt')

k = int(input())
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

ans = 0
for i in range(n - k):
    for j in range(i + k, n):
        ans = max(ans, a[i] + a[j])
print(ans)