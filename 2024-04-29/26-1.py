import sys
sys.stdin = open('26-1.txt')

k = int(input())
n = int(input())
a = []
for i in range(n):
    start, end = map(int, input().split())
    a.append([start, end])

a.sort()
cells = [-1] * k

cnt = 0

for i in a:
    for j in range(k):
        if cells[j] < i[0]:
            cnt += 1
            cells[j] = i[1]
            last = j + 1
            break
print(cnt)
print(last)