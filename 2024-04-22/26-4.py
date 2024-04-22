import sys
sys.stdin = open('26-4.txt')

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

a.sort(reverse=True)
b = [a[0]]
for i in a:
    if b[-1] - i >= 3:
        b.append(i)
print(len(b), b[-1])