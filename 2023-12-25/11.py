def f(start, end):
    a[start] = 1
    for i in range(start + 1, end + 1):
        a[i] = a[i - 1]
        if i % 2 == 0 and i // 2 >= start:
            a[i] += a[i // 2]
    return a[end]

a = [0] * 21
print(f(1, 10) * f(10, 20))