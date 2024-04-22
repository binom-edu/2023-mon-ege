import sys
sys.stdin = open('kurs-26-1.txt')

s, n = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))
a.sort()

disk = []
for i in a:
    if sum(disk) + i <= s:
        disk.append(i)
    else:
        break

print(len(disk))
disk.pop()
delta = s - sum(disk)
print(max([i for i in a if i <= delta]))