import sys
sys.stdin = open('26-2.txt')

n = int(input())
events = []
for i in range(n):
    start, end = map(int, input().split())
    events.append([start, end])

events.sort()

cnt = 1
end = events[0][1]
prev = 0

for event in events:
    if event[0] >= end:
        cnt += 1
        prev = end
        end = event[1]
    elif event[1] < end:
        end = event[1]

ans2 = 0
for event in events:
    if event[0] >= prev and event[1] > ans2:
        ans2 = event[1]
print(cnt, ans2)