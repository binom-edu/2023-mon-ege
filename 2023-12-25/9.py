a = [0] * 15
a[1] = 1
for i in range(2, 15):
    a[i] = a[i - 1]
    if i > 2:
        a[i] += a[i - 3]
print(a[14])