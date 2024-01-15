ans = set()
for x in range(500, 5000 + 1):
    b = bin(x)[3:]
    ans.add(x - int(b, 2))
print(len(ans))
print(ans)