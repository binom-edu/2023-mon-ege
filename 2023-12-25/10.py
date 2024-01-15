# команды: +1, *2
# сделать из 1 10, потом из 10 20

a = [0] * 21
a[1] = 1
for i in range(2, 11):
    a[i] = a[i - 1]
    if i % 2 == 0:
        a[i] += a[i // 2]
ans1 = a[10]

a = [0] * 21
a[10] = 1
for i in range(11, 21):
    a[i] = a[i - 1]
    if i % 2 == 0:
        a[i] += a[i // 2]
ans2 = a[20]
print(ans1 * ans2)