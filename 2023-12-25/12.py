# +1, *2, +3, сделать из 3 16, минуя 7 и 11
def f(start, end):
    a[start] = 1
    for i in range(start + 1, end + 1):
        if i in restricted:
            continue
        a[i] = a[i - 1]
        if i - 3 >= start:
            a[i] += a[i - 3]
        if i % 2 == 0 and i // 2 >= start:
            a[i] += a[i // 2]
    return a[end]

a = [0] * 17
restricted = [7, 11]
print(f(3, 16))