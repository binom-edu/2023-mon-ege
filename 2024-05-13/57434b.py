import sys
from collections import deque

sys.stdin = open('57434b.txt')

k = int(input())
n = int(input())
buf = deque()
for i in range(k):
    buf.append(int(input()))

ans = 0
max_x = 0
for i in range(n - k):
    y = int(input())
    x = buf.popleft()
    max_x = max(max_x, x)
    ans = max(ans, y + max_x)
    buf.append(y)
print(ans)